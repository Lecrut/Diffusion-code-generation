def are_lists_equal_by_hash(list1, list2):
    return hash(tuple(list1)) == hash(tuple(list2))
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 2, 3, 4, 6]
    print(are_lists_equal_by_hash(sample_list1, sample_list2))
    print(are_lists_equal_by_hash(sample_list1, sample_list3))