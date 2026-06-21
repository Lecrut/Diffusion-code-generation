def are_lists_equal_by_hash(list1, list2):
    if len(list1) != len(list2):
        return False
    hash_list1 = hash(tuple(list1))
    hash_list2 = hash(tuple(list2))
    return hash_list1 == hash_list2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    print(are_lists_equal_by_hash(sample_list1, sample_list2))
    sample_list3 = [1, 2, 3, 4, 5]
    sample_list4 = [1, 2, 3, 4, 6]
    print(are_lists_equal_by_hash(sample_list3, sample_list4))