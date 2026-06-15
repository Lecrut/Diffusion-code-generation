def compare_sorted_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] != list2[j]:
            return (list1[i], list2[j])
        i += 1
        j += 1
    if i < n:
        return (list1[i], "End of list2")
    elif j < m:
        return ("End of list1", list2[j])
    else:
        return ("Lists are identical")
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 5, 8, 9]
    print(compare_sorted_lists(list_a, list_b))
    list_c = [1, 2, 3, 4]
    list_d = [1, 2, 3]
    print(compare_sorted_lists(list_c, list_d))
    list_e = [10, 20, 30]
    list_f = [10, 20, 30]
    print(compare_sorted_lists(list_e, list_f))
    list_g = [5, 6, 7]
    list_h = [5, 8, 9]
    print(compare_sorted_lists(list_g, list_h))