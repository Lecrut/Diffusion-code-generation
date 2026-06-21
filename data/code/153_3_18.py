def check_target_exists(data, target):
    return any(item == target for item in data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_value = 35
    result = check_target_exists(sample_list, target_value)
    print(result)

    sample_list_2 = [15, 25, 35, 45, 55]
    target_value_2 = 35
    result_2 = check_target_exists(sample_list_2, target_value_2)
    print(result_2)