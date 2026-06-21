def binary_search(arr, target):
    if not arr:
        raise ValueError("Array cannot be empty")
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("Target not found in array")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_value = 7
    result = binary_search(sample_list, target_value)
    print(f"Index of {target_value} in the list: {result}")