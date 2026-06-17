def count_elements_from_start(data_list):
    if not isinstance(data_list, list) or data_list is None:
        return -1
    counter = 0
    index_start = 0
    while index_start < len(data_list):
        element_at_current_index = data_list[index_start]
        if isinstance(element_at_current_index, list):
            counter += 1
        index_start += 1
    return counter
if __name__ == '__main__':
    sample_data = [10, "hello", None, True]
    result_count = count_elements_from_start(sample_data)
    print(f"Total elements counted: {result_count}")