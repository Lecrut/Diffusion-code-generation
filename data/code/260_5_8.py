def compare_sorted_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    min_len = min(len1, len2)
    for i in range(min_len):
        if list1[i] != list2[i]:
            return (f"Divergence at index {i}: list1[{i}]={list1[i]}, list2[{i}]={list2[i]}")
    if len1 != len2:
        return f"Length mismatch. list1 length: {len1}, list2 length: {len2}"
    return "Lists are identical"
if __name__ == '__main__':
    list_a = [1, 5, 8, 10, 12]
    list_b = [1, 5, 9, 10, 13]
    list_c = [1, 5, 8, 10]
    list_d = [1, 5, 8, 10, 12]
    list_e = [1, 5, 8, 10, 14]
    print(f"Comparing {list_a} and {list_b}: {compare_sorted_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_sorted_lists(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_d}: {compare_sorted_lists(list_d, list_d)}")
    print(f"Comparing {list_e} and {list_a}: {compare_sorted_lists(list_e, list_a)}")