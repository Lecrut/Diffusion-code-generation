def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for elem1, elem2 in zip(list1, list2):
        if elem1 != elem2:
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 4, 5]
    list_c = [1, 2, 3, 4, 6]
    result_ab = are_lists_identical(list_a, list_b)
    result_ac = are_lists_identical(list_a, list_c)
    print(result_ab)
    print(result_ac)