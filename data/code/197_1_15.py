def binary_search(data_list, element):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == element:
            return True
        elif data_list[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return False

def validate_input(data_list, element):
    if not isinstance(data_list, list) or not all(isinstance(item, (int, str)) for item in data_list):
        raise ValueError("data_list must be a list of integers or strings")
    if not isinstance(element, (int, str)):
        raise ValueError("element must be an integer or string")

def check_membership(data_list, element):
    validate_input(data_list, element)
    return binary_search(sorted(data_list), element)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    element1 = 8
    print(f"List: {list1}, Element: {element1}, Result: {check_membership(list1, element1)}")
    
    list2 = ['a', 'b', 'c']
    element2 = 'd'
    print(f"List: {list2}, Element: {element2}, Result: {check_membership(list2, element2)}")
    
    list3 = [10, 20, 30]
    element3 = 20
    print(f"List: {list3}, Element: {element3}, Result: {check_membership(list3, element3)}")