def find_last_occurrence(lst, element):
    for i in reversed(range(len(lst))):
        if lst[i] == element:
            return i
    return -1
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 30, 60, 30]
    target_element = 30
    result_index = find_last_occurrence(sample_list, target_element)
    print(result_index)
    empty_list = []
    not_found_result = find_last_occurrence(empty_list, 10)
    print(not_found_result)
    single_element_list = [42]
    single_result = find_last_occurrence(single_element_list, 42)
    print(single_result)
    no_match_list = [1, 2, 3, 4, 5]
    no_match_result = find_last_occurrence(no_match_list, 6)
    print(no_match_result)