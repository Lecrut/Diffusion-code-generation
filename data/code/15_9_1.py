def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 4, 5]
    list_c = [1, 2, 3, 5, 4]
    list_d = [1, 2, 3, 4]
    list_e = [1, 2, 3, 4, 5, 6]
    list_f = [1, 2, 3, 4, 5]
    print(f"list_a and list_b are identical: {are_lists_identical(list_a, list_b)}")
    print(f"list_a and list_c are identical: {are_lists_identical(list_a, list_c)}")
    print(f"list_a and list_d are identical: {are_lists_identical(list_a, list_d)}")
    print(f"list_a and list_e are identical: {are_lists_identical(list_a, list_e)}")
    print(f"list_a and list_f are identical: {are_lists_identical(list_a, list_f)}")