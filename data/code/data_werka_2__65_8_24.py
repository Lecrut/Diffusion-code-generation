def get_element_by_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    
    INDEX_OUT_OF_BOUNDS_MESSAGE = "Index out of bounds"
    
    if index < 0 or index >= len(lst):
        raise IndexError(INDEX_OUT_OF_BOUNDS_MESSAGE)
    
    return lst[index]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    VALID_INDEX = 2
    INVALID_INDEX = 5
    
    try:
        element = get_element_by_position(SAMPLE_LIST, VALID_INDEX)
        print(f"Element at index {VALID_INDEX}: {element}")
    except IndexError as e:
        print(e)
    
    try:
        element = get_element_by_position(SAMPLE_LIST, INVALID_INDEX)
        print(f"Element at index {INVALID_INDEX}: {element}")
    except IndexError as e:
        print(e)