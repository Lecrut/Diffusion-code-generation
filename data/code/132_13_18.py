def are_lists_identical(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError('Both inputs must be lists.')
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if type(item1) is not type(item2):
            return False
        elif isinstance(item1, list) and isinstance(item2, list):
            if not are_lists_identical(item1, item2):
                return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, [3, 4], 5]
    sample_list2 = [1, 2, [3, 4], 5]
    print(are_lists_identical(sample_list1, sample_list2))
    sample_list3 = [1, 2, [3, 4], 5]
    sample_list4 = [1, 2, [3, 5], 5]
    print(are_lists_identical(sample_list3, sample_list4))
    sample_list5 = [1, 2, [3, 4], 5]
    sample_list6 = [1, 2, [3, 4]]
    print(are_lists_identical(sample_list5, sample_list6))