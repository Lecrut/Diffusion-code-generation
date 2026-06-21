if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = any(value == target_value for value in sample_list)
    print(result)
    sample_list_2 = [10, 20, 30, 10, 40, 10]
    target_value_2 = 10
    result_2 = any(value == target_value_2 for value in sample_list_2)
    print(result_2)
    sample_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_3 = any(value == target_value_3 for value in sample_list_3)
    print(result_3)