import BinarySearch as binary
import Bubblesort as bubble

def villainSearch(villains):
    query = input(f"Input a villains name to see if they're in the dataset: ")
    binary.check(villains, query, len(villains), 0, -1)

    def options():
        result = input("Input 'retry' to perform the search again on the same list, 'refresh' to input a new list, or 'exit' to exit the program: ")
        if result == "exit":
            quit()
        elif result == "retry":
            villainSearch(villains)
        elif result == "refresh":
            fileParse()
        else:
            print("Sorry, the entered value doesn't match any of the commands specified above. Please try again.\n")
            options()
    options()

def fileParse():
    filefound = False
    while filefound == False:
            file = input("Please enter the name of the .txt file being used for this operation: ")
            villains = open(f"{file}.txt", "r").read().splitlines()
            sortedVillains = bubble.sort(villains)
            print(f"Unsorted data: {villains}\n")
            print(f"Sorted data: {sortedVillains}\n")
            filefound = True
            return villainSearch(sortedVillains)
  
fileParse()