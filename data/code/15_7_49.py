def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    example_list1 = [100, 200, 300, 400, 500]
    example_list2 = [100, 200, 300, 400, 500]
    example_list3 = [100, 200, 300, 400, 600]
    print(are_lists_identical(example_list1, example_list2))
    print(are_lists_identical(example_list1, example_list3))