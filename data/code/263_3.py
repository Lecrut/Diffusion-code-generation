def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 5, 3]
    list_b = [1, 6, 4]
    result1 = compare_lists(list_a, list_b)
    print(result1)
    list_c = [2, 4, 5]
    list_d = [2, 3, 4]
    result2 = compare_lists(list_c, list_d)
    print(result2)
    list_e = [10, 20]
    list_f = [5, 15]
    result3 = compare_lists(list_e, list_f)
    print(result3)
    list_g = [1, 2, 3]
    list_h = [1, 2, 4]
    result4 = compare_lists(list_g, list_h)
    print(result4)