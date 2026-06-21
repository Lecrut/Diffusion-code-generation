def contains_target(data, target):
    return any((item == target for item in data))
if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = contains_target(sample_list, target_value)
    print(result)
    sample_list_2 = [10, 20, 30, 10, 40, 10]
    target_value_2 = 99
    result_2 = contains_target(sample_list_2, target_value_2)
    print(result_2)