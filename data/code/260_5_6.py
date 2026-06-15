def compare_sorted_lists(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    min_len = min(n1, n2)
    for i in range(min_len):
        if list1[i] != list2[i]:
            return i
    if n1 != n2:
        return min_len
    return min_len
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 5, 8, 9]
    result1 = compare_sorted_lists(list_a, list_b)
    print(f"Comparison of {list_a} and {list_b}: First divergence at index {result1}")
    list_c = [1, 2, 3, 4]
    list_d = [1, 2, 3]
    result2 = compare_sorted_lists(list_c, list_d)
    print(f"Comparison of {list_c} and {list_d}: First divergence at index {result2}")
    list_e = [10, 20]
    list_f = [10, 20]
    result3 = compare_sorted_lists(list_e, list_f)
    print(f"Comparison of {list_e} and {list_f}: First divergence at index {result3}")
    list_g = [1, 2, 3]
    list_h = [1, 2, 4]
    result4 = compare_sorted_lists(list_g, list_h)
    print(f"Comparison of {list_g} and {list_h}: First divergence at index {result4}")