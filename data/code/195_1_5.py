def list_comparison(list1, list2):
    if len(list1) != len(list2):
        mismatches = []
        for i in range(min(len(list1), len(list2))):
            mismatches.append(i)
        return {'mismatch_indices': mismatches}
    mismatches = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            mismatches.append(i)
    if not mismatches:
        return {'result': 'same'}
    else:
        return {'mismatch_indices': mismatches}
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 9, 4]
    list_d = [1, 2, 3]
    list_e = [1, 2, 3, 4, 5]
    print(f"Comparing {list_a} and {list_b}: {list_comparison(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {list_comparison(list_a, list_c)}")
    print(f"Comparing {list_a} and {list_d}: {list_comparison(list_a, list_d)}")
    print(f"Comparing {list_a} and {list_e}: {list_comparison(list_a, list_e)}")
    list_f = [10, 20]
    list_g = [10, 20, 30]
    print(f"Comparing {list_f} and {list_g}: {list_comparison(list_f, list_g)}")