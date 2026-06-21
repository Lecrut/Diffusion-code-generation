def get_first_element(lst):
    EMPTY_LIST_ERROR_MESSAGE = "The input list is empty"
    if not lst:
        raise ValueError(EMPTY_LIST_ERROR_MESSAGE)
    return lst[0]

if __name__ == '__main__':
    SAMPLE_LIST = [15, 25, 35, 45, 55]
    try:
        print(get_first_element(SAMPLE_LIST))
    except ValueError as e:
        print(e)

    EMPTY_LIST = []
    try:
        print(get_first_element(EMPTY_LIST))
    except ValueError as e:
        print(e)

    SINGLE_ELEMENT_LIST = [100]
    try:
        print(get_first_element(SINGLE_ELEMENT_LIST))
    except ValueError as e:
        print(e)