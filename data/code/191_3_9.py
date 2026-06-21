def extend_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'value': 'A'}]
    sample_list2 = [{'id': 2, 'value': 'B'}, {'id': 3, 'value': 'C'}]
    result = extend_lists(sample_list1, sample_list2)
    print(result)