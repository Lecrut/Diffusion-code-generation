def is_in_frozenset(element, frozenset_):
    return element in frozenset_
if __name__ == '__main__':
    sample_set = frozenset([1, 2, 3, 4, 5])
    print(is_in_frozenset(3, sample_set))
    print(is_in_frozenset(6, sample_set))