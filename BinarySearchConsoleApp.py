def display_title_bar():
    # Display a title.
    print("\n")
    print("\t**********************************************")
    print("\t**************  Binary Search  ***************")
    print("\t**********************************************")
    print("\n")

def fillList():
    # creating a list
    lst = []
    
    # number of elements
    n = int(input("Enter the number of elements: "))
    
    # iterating 
    for i in range(0, n):
        ele = int(input("Enter the elements (only numbers) : "))
    
        lst.append(ele) 
        
    return lst

def binarySearchIterative():
    elems=fillList()
    target = int(input("Enter the number to search: "))
    left = 0
    right = len(elems)-1
    while left <= right:
        middle=(left+right)//2

        if elems[middle]==target:
            print(elems)
            print("Target found in index: ", middle)
            break

        if elems[middle]< target:
            left=middle+1
        elif elems[middle]> target:
            right=middle-1
    
    if left>right:
        print("Not found")

def binarySearchRecursive():
    elems=fillList()
    target = int(input("Enter the number to search: "))

    def search(elems, target):
        left, right = 0, len(elems) - 1

        if left <= right:
            middle = (left + right) // 2

            if elems[middle] == target:
                print(elems)
                print("Target found in index: ", middle)
                
            if elems[middle] < target:
                return search(elems[middle + 1:], target)
            elif elems[middle] > target:
                return search(elems[:middle], target)

        if left>right:
            print("Not found")
    
    search(elems, target)


choice = ''
display_title_bar()

while choice != 'q':    
    # Let users know what they can do.
    print("\n[1] Iteratively")
    print("[2] Recursively")
    print("[q] Quit.")
    
    choice = input("\nHow do you want to search? (Choose an option) ")

    # Respond to the user's choice.
    if choice == '1':
        binarySearchIterative()
        display_title_bar()
    elif choice == '2':
        binarySearchRecursive()
        display_title_bar()
    elif choice == 'q':
        print("\nAdiós!")
    else:
        print("\nI didn't understand that choice.\n")