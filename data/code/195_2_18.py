def are_lists_equal(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    return sorted_list1 == sorted_list2

if __name__ == '__main__':
    sample_list1 = [4, 3, 2, 1]
    sample_list2 = [1, 2, 3, 4]
    sample_list3 = [1, 2, 3, 5]
    print(f"sample_list1 == sample_list2: {are_lists_equal(sample_list1, sample_list2)}")
    print(f"sample_list1 == sample_list3: {are_lists_equal(sample_list1, sample_list3)}")