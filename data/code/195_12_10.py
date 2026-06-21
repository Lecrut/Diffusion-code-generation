def deep_compare(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if isinstance(item1, list) and isinstance(item2, list):
            if not deep_compare(item1, item2):
                return False
        elif item1 != item2:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, [2, 3], [4, [5, 6]]]
    sample_list2 = [1, [2, 3], [4, [5, 6]]]
    print(deep_compare(sample_list1, sample_list2))
    sample_list3 = [1, [2, 3], [4, [5, 7]]]
    print(deep_compare(sample_list1, sample_list3))