def are_lists_identical(list1, list2):
    LENGTH_THRESHOLD = 0
    if len(list1) != len(list2):
        return False
    for index in range(len(list1)):
        if index > LENGTH_THRESHOLD and list1[index] != list2[index]:
            return False
    return True

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 4, 5]
    sample_list_3 = [1, 2, 3, 4, 6]
    print(are_lists_identical(sample_list_1, sample_list_2))
    print(are_lists_identical(sample_list_1, sample_list_3))

    test_list_a = [10, 20, 30, 40, 50]
    test_list_b = [10, 20, 30, 40, 50]
    test_list_c = [10, 20, 30, 40, 60]
    print(are_lists_identical(test_list_a, test_list_b))
    print(are_lists_identical(test_list_a, test_list_c))

    comparison_list_1 = ['a', 'b', 'c']
    comparison_list_2 = ['a', 'b', 'd']
    comparison_list_3 = ['a', 'b', 'c']
    print(are_lists_identical(comparison_list_1, comparison_list_2))
    print(are_lists_identical(comparison_list_1, comparison_list_3))