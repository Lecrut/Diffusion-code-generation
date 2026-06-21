def combine_and_extend(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list_a = [{'a': 1}, {'b': 2}]
    sample_list_b = [{'c': 3}, {'d': 4}]
    result = combine_and_extend(sample_list_a, sample_list_b)
    print(result)