def list_comparison(list1, list2):
    if len(list1) != len(list2):
        mismatches = []
        for i in range(min(len(list1), len(list2))):
            mismatches.append(i)
        return {"mismatch_indices": mismatches}
    mismatched_indices = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            mismatched_indices.append(i)
    if not mismatched_indices:
        return "same"
    else:
        return {"mismatch_indices": mismatched_indices}
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    result1 = list_comparison(list_a, list_b)
    print(f"Comparing {list_a} and {list_b}: {result1}")
    list_c = [1, 2, 9, 4]
    list_d = [1, 2, 3, 4]
    result2 = list_comparison(list_c, list_d)
    print(f"Comparing {list_c} and {list_d}: {result2}")
    list_e = [1, 2]
    list_f = [1, 2, 3]
    result3 = list_comparison(list_e, list_f)
    print(f"Comparing {list_e} and {list_f}: {result3}")
    list_g = [5, 6]
    list_h = [5, 7]
    result4 = list_comparison(list_g, list_h)
    print(f"Comparing {list_g} and {list_h}: {result4}")