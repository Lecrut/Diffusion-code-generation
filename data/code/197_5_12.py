def is_element_in_frozenset(element, frozenset_obj):
    return element in frozenset_obj

if __name__ == '__main__':
    sample_element = 5
    sample_frozenset = frozenset([1, 3, 5, 7, 9])
    print(is_element_in_frozenset(sample_element, sample_frozenset))