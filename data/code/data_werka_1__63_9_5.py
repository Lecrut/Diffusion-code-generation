def get_first_element(data_list):
    if not data_list:
        raise ValueError("The input list is empty.")
    return data_list[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        result = get_first_element(sample_data)
        print(result)
    except ValueError as e:
        print(e)

    sample_data_empty = []
    try:
        result_empty = get_first_element(sample_data_empty)
        print(result_empty)
    except ValueError as e:
        print(e)

    sample_data_single = [99]
    try:
        result_single = get_first_element(sample_data_single)
        print(result_single)
    except ValueError as e:
        print(e)