def locate_last_occurrence_index(data_list, target):
    if not isinstance(data_list, list):
        raise ValueError("The first argument must be a list.")
    if not data_list:
        return -1
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 30]
    target_value = 30
    final_index = locate_last_occurrence_index(sample_data, target_value)
    print(final_index)

    sample_data_empty = []
    target_value_empty = 10
    final_index_empty = locate_last_occurrence_index(sample_data_empty, target_value_empty)
    print(final_index_empty)

    sample_data_single = [99]
    target_value_single = 99
    final_index_single = locate_last_occurrence_index(sample_data_single, target_value_single)
    print(final_index_single)

    sample_data_no_match = [10, 20, 30, 40, 50]
    target_value_no_match = 60
    final_index_no_match = locate_last_occurrence_index(sample_data_no_match, target_value_no_match)
    print(final_index_no_match)