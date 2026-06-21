def unique_common_items(list1, list2):
    set1 = set(filter(lambda x: isinstance(x, hashable), list1))
    set2 = set(filter(lambda x: isinstance(x, hashable), list2))
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, '3', (4,), 5]
    sample_list2 = [4, 5, '6', (7,), 8]
    common_items = unique_common_items(sample_list1, sample_list2)
    print(common_items)