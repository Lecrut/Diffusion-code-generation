def find_last_occurrence(lst, element):
    START_INDEX = len(lst) - 1
    END_INDEX = -1
    STEP_SIZE = -1
    
    for index in range(START_INDEX, END_INDEX, STEP_SIZE):
        if lst[index] == element:
            return index
    return -1

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    TARGET_ELEMENT = 30
    result = find_last_occurrence(SAMPLE_LIST, TARGET_ELEMENT)
    print(result)
    
    EMPTY_LIST = []
    target_empty = 5
    last_index_empty = find_last_occurrence(EMPTY_LIST, target_empty)
    print(last_index_empty)
    
    SINGLE_ELEMENT_LIST = [42]
    target_single = 42
    last_index_single = find_last_occurrence(SINGLE_ELEMENT_LIST, target_single)
    print(last_index_single)
    
    NOT_FOUND_TARGET = 150
    last_index_not_found = find_last_occurrence(SAMPLE_LIST, NOT_FOUND_TARGET)
    print(last_index_not_found)