def intersect_lists(list1, list2):
    return list(frozenset(list1) & frozenset(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [3, 4, 5, 6]
    print(intersect_lists(sample_list1, sample_list2))