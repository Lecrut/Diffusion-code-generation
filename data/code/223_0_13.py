MAX_VALUE = float('-inf')

def find_max_value(numbers):
    return max(numbers, default=MAX_VALUE)

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Maximum of {list1}: {find_max_value(list1)}")
    
    list2 = [-10, -5, -20, -1]
    print(f"Maximum of {list2}: {find_max_value(list2)}")
    
    list3 = [7]
    print(f"Maximum of {list3}: {find_max_value(list3)}")
    
    list4 = []
    print(f"Maximum of {list4}: {find_max_value(list4)}")