def is_element_in_frozenset(item, frozenset_obj):
    return item in frozenset_obj

if __name__ == '__main__':
    sample_set = frozenset([10, 20, 30, 40, 50])
    element_to_check_1 = 30
    element_to_check_2 = 60
    print(is_element_in_frozenset(element_to_check_1, sample_set))
    print(is_element_in_frozenset(element_to_check_2, sample_set))