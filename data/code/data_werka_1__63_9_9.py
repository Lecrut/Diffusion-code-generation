def get_first_element(data_list):
    if not data_list:
        raise ValueError("The input list is empty")
    return data_list[0]

if __name__ == '__main__':
    SAMPLE_DATA = [10, 20, 30, 40]
    try:
        result = get_first_element(SAMPLE_DATA)
        print(result)
    except ValueError as e:
        print(e)

    EMPTY_DATA = []
    try:
        result_empty = get_first_element(EMPTY_DATA)
        print(result_empty)
    except ValueError as e:
        print(e)

    SINGLE_ELEMENT_DATA = [99]
    try:
        result_single = get_first_element(SINGLE_ELEMENT_DATA)
        print(result_single)
    except ValueError as e:
        print(e)