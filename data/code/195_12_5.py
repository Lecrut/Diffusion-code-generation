def compare_lists(list1, list2):
    return set(list1) == set(list2) and sorted(list1) == sorted(list2)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    list_c = [1, 2, 3]
    list_d = [1, 2, 2, 4]
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_a}: {compare_lists(list_d, list_a)}")