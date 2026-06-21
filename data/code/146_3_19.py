def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    target_value = 5
    result = binary_search(sample_list, target_value)
    print(f"Index of {target_value}: {result}")

    empty_list = []
    target_value = 2
    result = binary_search(empty_list, target_value)
    print(f"Index in empty list: {result}")

    single_element_list = [42]
    target_value = 42
    result = binary_search(single_element_list, target_value)
    print(f"Index in single element list: {result}")