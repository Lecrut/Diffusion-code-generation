def is_element_in_frozenset(element, frozenset_obj):
    return element in frozenset_obj

if __name__ == '__main__':
    sample_set = frozenset([10, 20, 30, 40, 50])
    print(is_element_in_frozenset(30, sample_set))
    print(is_element_in_frozenset(60, sample_set))