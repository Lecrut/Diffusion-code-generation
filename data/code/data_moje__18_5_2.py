def find_middle(arr):
    if not arr:
        return None, None
    length = len(arr)
    middle_index = length // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [7],
        [5, 5, 5, 5],
        [1, 2, 3, 4, 5, 6]
    ]
    for case in test_cases:
        idx, val = find_middle(case)
        print(idx, val)