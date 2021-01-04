# Initialization
myUniqueList = []
myLeftovers = []

# Functions
def AddtoList(add):
    global myUniqueList, myLeftovers
    if add in myUniqueList:
        print("It's not unique, adding this to leftovers")
        myLeftovers.append(add)
    else:
        myUniqueList.append(add)

# Main Program
print("My Unique List = ", myUniqueList)
print("Let's add something unique to the list!")
add = input("Type something to add = ")
AddtoList(add)
repeat = input("Do you want to add something again? (y/n) ")
while repeat == "y":
    add = input("Type something to add = ")
    AddtoList(add)
    repeat = input("Do you want to add something again? (y/n) ")
    if repeat == "n":
        break
    elif repeat != "y" and repeat != "n":
        print("Wrong Command!")
        break    
print("My New Unique List = ", myUniqueList)
print("My Leftovers = ", myLeftovers)