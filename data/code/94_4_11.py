def _validate_input(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list")
    return True

def check_existence(data_list):
    _validate_input(data_list)
    if len(data_list) == 0:
        return False
    current_index = 0
    list_length = len(data_list)
    while current_index < list_length:
        if data_list[current_index] is True:
            return True
        current_index += 1
    return False

if __name__ == '__main__':
    sample_data_1 = [False, False, False]
    sample_data_2 = [False, True, False]
    sample_data_3 = []
    sample_data_4 = [True]
    sample_data_5 = [False, False, False, False]
    result_1 = check_existence(sample_data_1)
    result_2 = check_existence(sample_data_2)
    result_3 = check_existence(sample_data_3)
    result_4 = check_existence(sample_data_4)
    result_5 = check_existence(sample_data_5)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)