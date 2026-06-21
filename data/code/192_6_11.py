def intersect_lists(list1, list2):
    set1 = {item for item in list1 if isinstance(item, hashable_types)}
    set2 = {item for item in list2 if isinstance(item, hashable_types)}
    return list(set1.intersection(set2))

hashable_types = (int, float, str, tuple, frozenset)

if __name__ == '__main__':
    list_a = [1, 2, 'a', (3, 4), [5, 6], {7, 8}]
    list_b = ['a', 2, (3, 4), 9.0, (3, 4)]
    common = intersect_lists(list_a, list_b)
    print(common)