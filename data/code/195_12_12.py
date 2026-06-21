def compare_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return list1 == list2
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if not compare_lists(item1, item2):
            return False
    return True

if __name__ == '__main__':
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    list_c = [1, 2, 3]
    list_d = [1, 2, 2, 4]
    list_e = [1, 2, 2]
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_e}: {compare_lists(list_d, list_e)}")