def find_middle(arr):
    if not arr:
        return None, None
    middle_index = len(arr) // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    for case in test_cases:
        result = find_middle(case)
        print(result)