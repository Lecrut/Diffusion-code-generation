def find_middle_index_and_value(arr):
    if not arr:
        return None, None
    mid_index = len(arr) // 2
    mid_value = arr[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5, 7, 9],
        [10, 20, 30, 40, 50, 60],
        [5],
        [2, 4, 6, 8, 10, 12, 14],
        [100, 200]
    ]
    for case in test_cases:
        index, value = find_middle_index_and_value(case)
        print(f"Array: {case} | Middle Index: {index} | Middle Value: {value}")