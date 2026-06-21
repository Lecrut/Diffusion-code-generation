def intersect_lists(list1, list2):
    set1 = {item for item in list1 if isinstance(item, hashable)}
    set2 = {item for item in list2 if isinstance(item, hashable)}
    return list(set1.intersection(set2))

if __name__ == '__main__':
    list_a = [1, 2, 'a', (3, 4), 5]
    list_b = ['b', (3, 4), 5, 6]
    common = intersect_lists(list_a, list_b)
    print(common)