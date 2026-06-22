def merge_and_reverse_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples.")
    
    merged_list = list1 + list2
    return merged_list[::-1]

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = merge_and_reverse_lists(list_a, list_b)
    print(result)

    list_c = (7, 8, 9)
    list_d = (10, 11, 12)
    result = merge_and_reverse_lists(list_c, list_d)
    print(result)

    list_e = [13]
    list_f = []
    result = merge_and_reverse_lists(list_e, list_f)
    print(result)