def compare_nested_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if isinstance(list1[i], list) and isinstance(list2[i], list):
            if not compare_nested_lists(list1[i], list2[i]):
                return False
        elif list1[i] != list2[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, [3, 4, [5]], 6]
    sample_list2 = [1, 2, [3, 4, [5]], 6]
    print(compare_nested_lists(sample_list1, sample_list2))
    sample_list3 = [1, 2, [3, 4, [5]], 7]
    print(compare_nested_lists(sample_list1, sample_list3))