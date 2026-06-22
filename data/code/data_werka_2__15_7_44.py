def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
    return True
if __name__ == '__main__':
    example_list_1 = [100, 200, 300, 400, 500]
    example_list_2 = [100, 200, 300, 400, 500]
    example_list_3 = [100, 200, 300, 400, 600]
    print(are_lists_identical(example_list_1, example_list_2))
    print(are_lists_identical(example_list_1, example_list_3))