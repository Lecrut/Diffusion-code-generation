def validate_input(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise ValueError("List cannot be empty")

def find_max(data):
    validate_input(data)
    return max(data)

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    
    print(f"Max of {list1}: {find_max(list1)}")
    print(f"Max of {list2}: {find_max(list2)}")
    print(f"Max of {list3}: {find_max(list3)}")
    try:
        print(find_max(list4))
    except ValueError as e:
        print(e)