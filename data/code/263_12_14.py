def intersect_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError('Both inputs must be lists.')
    return [element for element in set(list1) & set(list2)]
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = intersect_lists(sample_list1, sample_list2)
    print(result)