def find_middle_index_and_value(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    middle_index = len(arr) // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [10, 20, 30, 40, 50],
        [1, 2, 3, 4, 5, 6],
        [7, 14, 21],
        [42],
        [5, 15, 25, 35, 45, 55, 65]
    ]
    for test_case in test_cases:
        index, value = find_middle_index_and_value(test_case)
        print(f"Array: {test_case} -> Middle Index: {index}, Middle Value: {value}")