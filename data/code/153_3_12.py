if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = any(x == target_value for x in sample_list)
    print(result)
    sample_list_2 = [10, 20, 30, 10, 40, 10]
    target_value_2 = 10
    result_2 = any(x == target_value_2 for x in sample_list_2)
    print(result_2)
    sample_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_3 = any(x == target_value_3 for x in sample_list_3)
    print(result_3)