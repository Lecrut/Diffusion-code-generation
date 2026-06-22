def get_middle_value(arr):
    if len(arr) == 0:
        raise ValueError("Array cannot be empty")
    return arr[len(arr) // 2]

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    result = get_middle_value(test_data)
    print(result)
    test_data_even = [1, 2, 3, 4]
    result_even = get_middle_value(test_data_even)
    print(result_even)