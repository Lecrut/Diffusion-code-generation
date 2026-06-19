def find_last_occurrence_index(data_list, target):
    NOT_FOUND = -1
    if not data_list:
        return NOT_FOUND
    
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == target:
            return index
    return NOT_FOUND

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 30]
    target_value = 30
    last_index = find_last_occurrence_index(sample_data, target_value)
    print(last_index)

    empty_list = []
    last_index_empty = find_last_occurrence_index(empty_list, target_value)
    print(last_index_empty)

    single_item_list = [42]
    last_index_single = find_last_occurrence_index(single_item_list, 42)
    print(last_index_single)

    non_existent_target = 99
    last_index_nonexistent = find_last_occurrence_index(sample_data, non_existent_target)
    print(last_index_nonexistent)