def compare_nested_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if isinstance(item1, list) and isinstance(item2, list):
            if not compare_nested_lists(item1, item2):
                return False
        elif item1 != item2:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, [3, 4], 5]
    sample_list2 = [1, 2, [3, 4], 5]
    print(compare_nested_lists(sample_list1, sample_list2))
    sample_list3 = [1, 2, [3, 4], 5]
    sample_list4 = [1, 2, [3, 5], 5]
    print(compare_nested_lists(sample_list3, sample_list4))