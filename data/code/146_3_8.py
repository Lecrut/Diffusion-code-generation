def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 9
    result = binary_search(sample_list, target_value)
    print(f"Target {target_value} found at index: {result}")

    empty_list = []
    target_value = 5
    result = binary_search(empty_list, target_value)
    print(f"Target {target_value} not found in empty list. Result: {result}")

    single_element_list = [42]
    target_value = 42
    result = binary_search(single_element_list, target_value)
    print(f"Single element list search for {target_value}. Result: {result}")