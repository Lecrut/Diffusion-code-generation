def find_middle_index_and_value(arr):
    if not arr:
        return None, None
    middle_index = len(arr) // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [5, 15, 25, 35, 45, 55],
        [7],
        [100, 200]
    ]
    for case in test_cases:
        result = find_middle_index_and_value(case)
        print(f"Array: {case}, Middle Index: {result[0]}, Middle Value: {result[1]}")