def find_middle_index_value(arr):
    if not arr:
        return None
    mid_index = len(arr) // 2
    return mid_index, arr[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [42],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for case in test_cases:
        result = find_middle_index_value(case)
        print(f"Array: {case} -> Middle Index: {result[0]}, Value: {result[1]}")