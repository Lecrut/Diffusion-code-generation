def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    SAMPLE_LIST = [7, 14, 21, 28, 35]
    INDEX_TO_ACCESS = 2
    OUT_OF_BOUNDS_INDEX = 10
    result = get_element_at_index(SAMPLE_LIST, INDEX_TO_ACCESS)
    print(result)
    result_out_of_bounds = get_element_at_index(SAMPLE_LIST, OUT_OF_BOUNDS_INDEX)
    print(result_out_of_bounds)