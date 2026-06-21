def is_in_frozenset(element, frozenset_obj):
    return element in frozenset_obj

if __name__ == '__main__':
    sample_element = 3
    sample_set = frozenset([1, 2, 3, 4, 5])
    print(is_in_frozenset(sample_element, sample_set))