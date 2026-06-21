def combine_and_extend_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list_a = [{'a': 1}, {'b': 2}]
    sample_list_b = [{'c': 3}, {'d': 4}]
    combined_result = combine_and_extend_lists(sample_list_a, sample_list_b)
    print(combined_result)