def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 2, 3, 4, 6]
    print(are_lists_identical(sample_list1, sample_list2))
    print(are_lists_identical(sample_list1, sample_list3))
    test_list_1 = [7, 8, 9, 10, 11]
    test_list_2 = [7, 8, 9, 10, 11]
    test_list_3 = [7, 8, 9, 10, 12]
    print(are_lists_identical(test_list_1, test_list_2))
    print(are_lists_identical(test_list_1, test_list_3))
    sample_list4 = [10, 20, 30, 40, 50]
    sample_list5 = [10, 20, 30, 40, 50]
    sample_list6 = [10, 20, 30, 40, 60]
    print(are_lists_identical(sample_list4, sample_list5))
    print(are_lists_identical(sample_list4, sample_list6))