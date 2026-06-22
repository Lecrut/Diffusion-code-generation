def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    test_list_1 = [7, 8, 9, 10, 11]
    test_list_2 = [7, 8, 9, 10, 11]
    test_list_3 = [7, 8, 9, 10, 12]
    
    print(are_lists_identical(test_list_1, test_list_2))
    print(are_lists_identical(test_list_1, test_list_3))