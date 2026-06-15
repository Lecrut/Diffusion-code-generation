from collections import Counter
def compare_lists_ignoring_order(list1, list2):
    freq1 = Counter(list1)
    freq2 = Counter(list2)
    return freq1 == freq2
if __name__ == '__main__':
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    list_c = [1, 2, 3]
    list_d = [1, 2, 2, 4]
    list_e = [1, 2, 2]
    print(f"Comparing {list_a} and {list_b}: {compare_lists_ignoring_order(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists_ignoring_order(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_e}: {compare_lists_ignoring_order(list_d, list_e)}")