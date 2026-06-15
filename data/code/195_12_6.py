def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 != set2:
        return False
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    return count1 == count2
if __name__ == '__main__':
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    list_c = [1, 2, 3]
    list_d = [1, 2, 2, 4]
    list_e = [1, 2, 2]
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_e}: {compare_lists(list_d, list_e)}")
    print(f"Comparing {list_a} and [1, 2, 3]: {compare_lists(list_a, [1, 2, 3])}")
    print(f"Comparing {list_b} and {list_a}: {compare_lists(list_b, list_a)}")