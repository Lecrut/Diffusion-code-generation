def get_element_safely(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    VALID_INDEX = 2
    INVALID_INDEX = 7
    
    result_valid = get_element_safely(SAMPLE_LIST, VALID_INDEX)
    result_invalid = get_element_safely(SAMPLE_LIST, INVALID_INDEX)
    
    print(f"List: {SAMPLE_LIST}")
    print(f"Element at index {VALID_INDEX}: {result_valid}")
    print(f"Element at index {INVALID_INDEX}: {result_invalid}")