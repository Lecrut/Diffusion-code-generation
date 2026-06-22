def find_middle_index_and_value(arr):
    n = len(arr)
    if n == 0:
        raise ValueError("Array is empty")
    if n % 2 == 1:
        middle_index = n // 2
        middle_value = arr[middle_index]
        return middle_index, middle_value
    else:
        lower_middle_index = n // 2 - 1
        upper_middle_index = n // 2
        lower_middle_value = arr[lower_middle_index]
        upper_middle_value = arr[upper_middle_index]
        return (lower_middle_index, upper_middle_index), (lower_middle_value, upper_middle_value)

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [10],
        [1, 2],
        [],
        [7, 8, 9, 10, 11, 12, 13]
    ]
    
    for i, arr in enumerate(test_cases):
        try:
            result = find_middle_index_and_value(arr)
            print(f"Test case {i+1}: {arr} -> {result}")
        except ValueError as e:
            print(f"Test case {i+1}: {arr} -> Error: {e}")