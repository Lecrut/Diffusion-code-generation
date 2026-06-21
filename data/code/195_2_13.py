def are_lists_equal(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 == set2

if __name__ == '__main__':
    sample_list1 = [3, 1, 4]
    sample_list2 = [4, 3, 1]
    sample_list3 = [1, 2, 3]
    
    print(f"sample_list1 is equal to sample_list2: {are_lists_equal(sample_list1, sample_list2)}")
    print(f"sample_list1 is equal to sample_list3: {are_lists_equal(sample_list1, sample_list3)}")