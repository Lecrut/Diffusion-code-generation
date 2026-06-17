def compare_sorted_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] < list2[j]:
            return "Divergence found: list1[{i}] < list2[{j}]"
        elif list1[i] > list2[j]:
            return "Divergence found: list1[{i}] > list2[{j}]"
        i += 1
        j += 1
    if i < n:
        return f"Divergence found: list2 has been fully compared, remaining in list1: {list1[i:]}"
    elif j < m:
        return f"Divergence found: list1 has been fully compared, remaining in list2: {list2[j:]}"
    else:
        return "Lists are identical"
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 5, 8, 9]
    print(compare_sorted_lists(list_a, list_b))
    list_c = [10, 20, 30]
    list_d = [10, 25, 35]
    print(compare_sorted_lists(list_c, list_d))
    list_e = [1, 2, 3]
    list_f = [1, 2, 4]
    print(compare_sorted_lists(list_e, list_f))
    list_g = [5, 6, 7]
    list_h = [1, 2, 3]
    print(compare_sorted_lists(list_g, list_h))
    list_i = [1, 2, 3]
    list_j = [1, 2, 3]
    print(compare_sorted_lists(list_i, list_j))