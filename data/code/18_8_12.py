def get_middle_value(arr):
    if not arr:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    test_data_1 = [1, 3, 5, 7, 9]
    test_data_2 = [10, 20, 30, 40, 50, 60]
    test_data_3 = [42]
    print(get_middle_value(test_data_1))
    print(get_middle_value(test_data_2))
    print(get_middle_value(test_data_3))
    print(get_middle_value([]))