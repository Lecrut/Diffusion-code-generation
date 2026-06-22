def get_middle_value(array):
    if len(array) == 0:
        raise ValueError("Array cannot be empty")
    index = len(array) // 2
    return array[index]

if __name__ == '__main__':
    test_data_odd = [10, 20, 30, 40, 50]
    test_data_even = [1, 2, 3, 4, 5, 6]
    test_data_single = [42]
    
    print(get_middle_value(test_data_odd))
    print(get_middle_value(test_data_even))
    print(get_middle_value(test_data_single))