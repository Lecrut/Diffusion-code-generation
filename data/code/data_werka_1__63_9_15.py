def get_first_element(data_list):
    if not data_list:
        raise ValueError("The input list is empty")
    return data_list[0]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40]
    EMPTY_LIST = []
    SINGLE_ELEMENT_LIST = [99]

    try:
        result = get_first_element(SAMPLE_LIST)
        print(result)
    except ValueError as e:
        print(e)

    try:
        empty_result = get_first_element(EMPTY_LIST)
        print(empty_result)
    except ValueError as e:
        print(e)

    result_single = get_first_element(SINGLE_ELEMENT_LIST)
    print(result_single)