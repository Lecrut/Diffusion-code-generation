def get_sublist(larger_list, start_index, end_index):
    INDEX_OUT_OF_RANGE = "Index out of range."
    START_AFTER_END = "Start index cannot be greater than end index."
    
    if not isinstance(larger_list, list):
        raise ValueError("The first argument must be a list.")
    if not (isinstance(start_index, int) and isinstance(end_index, int)):
        raise ValueError("Start and end indices must be integers.")
    if start_index < 0 or end_index >= len(larger_list):
        raise IndexError(INDEX_OUT_OF_RANGE)
    if start_index > end_index:
        raise ValueError(START_AFTER_END)
    
    return larger_list[start_index:end_index + 1]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    START_INDEX = 3
    END_INDEX = 7
    sub_list = get_sublist(SAMPLE_LIST, START_INDEX, END_INDEX)
    print(sub_list)