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
    list_b = [1, 2, 5, 8, 9]
    print(compare_sorted_lists(list_a, list_b))
    list_c = [10, 20, 30]
    list_d = [10, 25, 35]
    print(compare_sorted_lists(list_c, list_d))
    list_e = [1, 2, 3]
    list_f = [4, 5, 6]
    print(compare_sorted_lists(list_e, list_f))
    list_g = [1, 2, 3]
    list_h = [1, 2, 3]
    print(compare_sorted_lists(list_g, list_h))