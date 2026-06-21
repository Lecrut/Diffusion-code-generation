def concatenate_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    return list_a + list_b

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)