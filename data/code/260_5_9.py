def compare_sorted_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] < list2[j]:
            return (list1[i], "list1 is smaller")
        elif list1[i] > list2[j]:
            return (list1[i], "list2 is smaller")
        else:
            i += 1
            j += 1
    if i < n:
        return (list1[i], "list1 has remaining elements")
    elif j < m:
        return (list2[j], "list2 has remaining elements")
    else:
        return (None, "lists are identical")
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 6, 8, 10]
    result1 = compare_sorted_lists(list_a, list_b)
    print(f"Comparing {list_a} and {list_b}: {result1}")
    list_c = [1, 3, 5, 7, 9]
    list_d = [1, 3, 5, 7, 9]
    result2 = compare_sorted_lists(list_c, list_d)
    print(f"Comparing {list_c} and {list_d}: {result2}")
    list_e = [1, 2, 3]
    list_f = [1, 2, 3, 4]
    result3 = compare_sorted_lists(list_e, list_f)
    print(f"Comparing {list_e} and {list_f}: {result3}")
    list_g = [5, 6]
    list_h = [1, 2]
    result4 = compare_sorted_lists(list_g, list_h)
    print(f"Comparing {list_g} and {list_h}: {result4}")