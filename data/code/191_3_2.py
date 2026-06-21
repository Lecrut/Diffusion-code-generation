def combine_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    combined_list = combine_lists(sample_list1, sample_list2)
    print(combined_list)