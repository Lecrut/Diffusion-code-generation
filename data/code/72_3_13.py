def compare_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")
    
    for index in range(len(list1)):
        if list1[index] > list2[index]:
            print(f"List1[{index}] ({list1[index]}) is greater than List2[{index}] ({list2[index]})")

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [10, 25, 30, 50]
    compare_lists(list_a, list_b)