def find_common_hashable(list1, list2):
    return list(set(item for item in list1 if isinstance(item, hashable)) & set(item for item in list2 if isinstance(item, hashable)))

if __name__ == '__main__':
    list_a = [1, 2, (3, 4), 'a', 4, 5]
    list_b = [(3, 4), 4, 5, 6, 'b']
    common = find_common_hashable(list_a, list_b)
    print(common)