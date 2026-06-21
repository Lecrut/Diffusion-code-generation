def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50]
    sample_list_b = [40, 50, 60, 70, 80]
    common_items_ab = find_common_items(sample_list_a, sample_list_b)
    print(f"Intersection of {sample_list_a} and {sample_list_b}: {common_items_ab}")

    sample_list_c = ['red', 'green', 'blue']
    sample_list_d = ['green', 'yellow', 'black']
    common_items_cd = find_common_items(sample_list_c, sample_list_d)
    print(f"Intersection of {sample_list_c} and {sample_list_d}: {common_items_cd}")

    sample_list_e = [1.5, 2.5, 3.5]
    sample_list_f = [2.5, 3.5, 4.5]
    common_items_ef = find_common_items(sample_list_e, sample_list_f)
    print(f"Intersection of {sample_list_e} and {sample_list_f}: {common_items_ef}")