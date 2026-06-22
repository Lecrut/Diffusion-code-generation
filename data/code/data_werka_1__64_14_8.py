def find_last_occurrence_index(data_list, target):
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_data = [5, 3, 9, 3, 7, 3]
    target_value = 3
    last_index = find_last_occurrence_index(sample_data, target_value)
    print(last_index)

    empty_data = []
    target_empty = 10
    last_index_empty = find_last_occurrence_index(empty_data, target_empty)
    print(last_index_empty)

    single_data = [42]
    target_single = 42
    last_index_single = find_last_occurrence_index(single_data, target_single)
    print(last_index_single)

    not_found_data = [1, 2, 3]
    target_not_found = 4
    last_index_not_found = find_last_occurrence_index(not_found_data, target_not_found)
    print(last_index_not_found)