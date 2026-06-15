def compare_lists(list1, list2):
    n = min(len(list1), len(list2))
    for i in range(n):
        if list1[i] != list2[i]:
            return i
    if len(list1) != len(list2):
        return -1
    return -1
if __name__ == '__main__':
    list_a = [1, 5, 3, 7, 9]
    list_b = [1, 5, 4, 7, 9]
    result = compare_lists(list_a, list_b)
    print(result)
    list_c = [10, 20, 30]
    list_d = [10, 20, 30]
    result = compare_lists(list_c, list_d)
    print(result)
    list_e = [1, 2, 3]
    list_f = [1, 2]
    result = compare_lists(list_e, list_f)
    print(result)