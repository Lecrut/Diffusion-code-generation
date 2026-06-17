def compare_sorted_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] != list2[j]:
            return f"Divergence at index {i} in list1 (value {list1[i]}) and index {j} in list2 (value {list2[j]})"
        i += 1
        j += 1
    if i < n:
        return f"List1 has remaining elements starting from index {i}: {list1[i:]}"
    elif j < m:
        return f"List2 has remaining elements starting from index {j}: {list2[j:]}"
    else:
        return "Lists are identical"
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [1, 2, 5, 8, 9]
    list_c = [1, 3, 5, 7, 9]
    list_d = [1, 3, 5, 6, 9]
    list_e = [10, 20]
    print(f"Comparing {list_a} and {list_b}: {compare_sorted_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_sorted_lists(list_a, list_c)}")
    print(f"Comparing {list_a} and {list_d}: {compare_sorted_lists(list_a, list_d)}")
    print(f"Comparing {list_e} and {list_a}: {compare_sorted_lists(list_e, list_a)}")