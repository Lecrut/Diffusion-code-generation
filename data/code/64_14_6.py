def find_last_index(data, target):
    for index in range(len(data) - 1, -1, -1):
        if data[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_data = [5, 3, 2, 7, 3, 9]
    target_value = 3
    last_index = find_last_index(sample_data, target_value)
    print(last_index)

    empty_list = []
    last_index_empty = find_last_index(empty_list, 3)
    print(last_index_empty)

    single_element_list = [8]
    last_index_single = find_last_index(single_element_list, 8)
    print(last_index_single)

    not_found_target = 10
    last_index_not_found = find_last_index(sample_data, not_found_target)
    print(last_index_not_found)