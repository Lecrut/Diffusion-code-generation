def lists_equal_by_hash(list1, list2):
    return hash(tuple(sorted(list1))) == hash(tuple(sorted(list2)))
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9]
    sample_list2 = [3, 1, 4, 1, 5, 9]
    sample_list3 = [3, 1, 4, 1, 6, 2]
    print(lists_equal_by_hash(sample_list1, sample_list2))
    print(lists_equal_by_hash(sample_list1, sample_list3))