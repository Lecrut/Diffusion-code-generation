def binary_search(arr, target):
    left, right = (0, len(arr) - 1)
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
    print(result)