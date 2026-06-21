def find_middle(arr):
    if not arr:
        return -1, None
    index = len(arr) // 2
    value = arr[index]
    return index, value

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 3),
        ([10, 20, 30, 40], 2, 30),
        ([100], 0, 100),
        ([5, 15, 25, 35, 45, 55], 3, 35)
    ]
    for arr, expected_index, expected_value in test_cases:
        index, value = find_middle(arr)
        print(index, value)