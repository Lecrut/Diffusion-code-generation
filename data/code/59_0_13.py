def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements in the list must be integers.")

def find_middle_item(data):
    validate_input(data)
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45]
    print(find_middle_item(list1))
    print(find_middle_item(list2))
    print(find_middle_item(list3))
    print(find_middle_item(list4))