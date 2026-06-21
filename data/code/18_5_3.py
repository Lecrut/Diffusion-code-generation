def find_middle_index_and_value(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    middle_index = len(arr) // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7, 9, 2, 8, 5, 3, 1],
        [42],
        [5, 15, 25, 35, 45, 55, 65, 75]
    ]
    for test in test_cases:
        index, value = find_middle_index_and_value(test)
        print(f"Array: {test}, Middle Index: {index}, Middle Value: {value}")