def find_last_occurrence(lst, element):
    try:
        return len(lst) - 1 - lst[::-1].index(element)
    except ValueError:
        return -1

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 30, 60, 30]
    target_element = 30
    result = find_last_occurrence(sample_list, target_element)
    print(result)

    empty_list = []
    target_empty = 10
    last_index_empty = find_last_occurrence(empty_list, target_empty)
    print(last_index_empty)

    single_element_list = [8]
    target_single = 8
    last_index_single = find_last_occurrence(single_element_list, target_single)
    print(last_index_single)

    not_found_target = 100
    last_index_not_found = find_last_occurrence(sample_list, not_found_target)
    print(last_index_not_found)