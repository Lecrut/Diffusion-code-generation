def find_common_hashable(list1, list2):
    set1 = {item for item in list1 if isinstance(item, hashable)}
    set2 = {item for item in list2 if isinstance(item, hashable)}
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    list_a = [1, 2, 'a', (3,), {4}, 5]
    list_b = ['a', 5, (3,), 6, 7]
    common = find_common_hashable(list_a, list_b)
    print(common)