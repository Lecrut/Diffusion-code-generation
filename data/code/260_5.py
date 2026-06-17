def compare_sorted_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] < list2[j]:
            return (list1[i], "list1 is smaller at index", i)
        elif list1[i] > list2[j]:
            return (list1[i], "list2 is smaller at index", j)
        else:
            i += 1
            j += 1
    if i < n:
        return (list1[i], "list1 has remaining elements", i)
    elif j < m:
        return (list2[j], "list2 has remaining elements", j)
    else:
        return (None, "lists are identical", -1)
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 6, 8, 10]
    result = compare_sorted_lists(list_a, list_b)
    print(result)
    list_c = [1, 2, 3, 4]
    list_d = [1, 2, 3, 5]
    result2 = compare_sorted_lists(list_c, list_d)
    print(result2)
    list_e = [10, 20, 30]
    list_f = [10, 20, 40]
    result3 = compare_sorted_lists(list_e, list_f)
    print(result3)
    list_g = [5, 6, 7]
    list_h = [1, 2, 3]
    result4 = compare_sorted_lists(list_g, list_h)
    print(result4)