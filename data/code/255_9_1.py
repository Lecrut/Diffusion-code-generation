def find_max_iterative(data_list, comparison_func):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    current_max = data_list[0]
    for i in range(1, len(data_list)):
        current_element = data_list[i]
        if comparison_func(current_element, current_max):
            current_max = current_element
    return current_max
def compare_strings(a, b):
    if isinstance(a, str) and isinstance(b, str):
        if a > b:
            return True
        elif a < b:
            return False
        else:
            return False
    return NotImplemented
def find_max_of_strings(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    current_max = data_list[0]
    for i in range(1, len(data_list)):
        current_element = data_list[i]
        if compare_strings(current_element, current_max):
            current_max = current_element
    return current_max
if __name__ == '__main__':
    list1 = ["apple", "zebra", "banana", "kiwi"]
    print(f"List 1: {list1}")
    max1 = find_max_of_strings(list1)
    print(f"Maximum element in List 1: {max1}")
    list2 = ["c", "a", "b", "d", "e"]
    print(f"\nList 2: {list2}")
    max2 = find_max_of_strings(list2)
    print(f"Maximum element in List 2: {max2}")
    list3 = ["red", "blue", "green"]
    print(f"\nList 3: {list3}")
    max3 = find_max_of_strings(list3)
    print(f"Maximum element in List 3: {max3}")