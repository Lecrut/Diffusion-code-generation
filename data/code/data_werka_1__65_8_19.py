def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds for list of length {len(lst)}") from e

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_ACCESS = 2
    INDEX_OUT_OF_BOUNDS = 5
    INDEX_NEGATIVE = -1

    try:
        value = get_element_by_position(SAMPLE_LIST, INDEX_TO_ACCESS)
        print(f"Value at index {INDEX_TO_ACCESS}: {value}")
    except IndexError as e:
        print(e)

    try:
        value = get_element_by_position(SAMPLE_LIST, INDEX_OUT_OF_BOUNDS)
        print(f"Value at index {INDEX_OUT_OF_BOUNDS}: {value}")
    except IndexError as e:
        print(e)

    try:
        value = get_element_by_position(SAMPLE_LIST, INDEX_NEGATIVE)
        print(f"Value at index {INDEX_NEGATIVE}: {value}")
    except IndexError as e:
        print(e)