def is_in_frozenset(element, frozenset_obj):
    if not isinstance(frozenset_obj, frozenset):
        raise ValueError("The second argument must be a frozenset.")
    return element in frozenset_obj

if __name__ == '__main__':
    sample_set = frozenset([1, 2, 3, 4, 5])
    print(is_in_frozenset(3, sample_set))
    print(is_in_frozenset(6, sample_set))