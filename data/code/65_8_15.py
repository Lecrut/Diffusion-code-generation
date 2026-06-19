def get_element_by_position(data_list, index):
    try:
        return data_list[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds.") from e

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    VALID_INDEX = 2
    INVALID_INDEX_OUT_OF_BOUNDS = 5
    INVALID_INDEX_NEGATIVE = -6

    try:
        print(get_element_by_position(SAMPLE_LIST, VALID_INDEX))
    except IndexError as e:
        print(e)

    try:
        print(get_element_by_position(SAMPLE_LIST, INVALID_INDEX_OUT_OF_BOUNDS))
    except IndexError as e:
        print(e)

    try:
        print(get_element_by_position(SAMPLE_LIST, INVALID_INDEX_NEGATIVE))
    except IndexError as e:
        print(e)