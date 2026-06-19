def validate_list(data_list):
    if not data_list:
        raise ValueError("The input list is empty")

def get_first_element(data_list):
    validate_list(data_list)
    return data_list[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result = get_first_element(sample_data)
    print(result)

    try:
        empty_data = []
        result_empty = get_first_element(empty_data)
        print(result_empty)
    except ValueError as e:
        print(e)

    sample_data_single = [99]
    result_single = get_first_element(sample_data_single)
    print(result_single)