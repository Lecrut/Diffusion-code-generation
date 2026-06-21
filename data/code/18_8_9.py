def get_middle_value(arr):
    if not arr:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    test_data_odd = [10, 20, 30, 40, 50]
    test_data_even = [1, 2, 3, 4, 5, 6]
    test_data_single = [42]
    test_data_empty = []
    
    print(get_middle_value(test_data_odd))
    print(get_middle_value(test_data_even))
    print(get_middle_value(test_data_single))
    print(get_middle_value(test_data_empty))