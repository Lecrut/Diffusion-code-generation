def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [100, 200, 300, 400, 500]
    INDEX_TO_FETCH = 2
    element = get_element_by_position(SAMPLE_LIST, INDEX_TO_FETCH)
    print(element)
    
    OUT_OF_BOUNDS_INDEX = 10
    element_out_of_bounds = get_element_by_position(SAMPLE_LIST, OUT_OF_BOUNDS_INDEX)
    print(element_out_of_bounds)