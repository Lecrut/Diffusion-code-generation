import collections
def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 != set2:
        return False
    counts1 = collections.Counter(list1)
    counts2 = collections.Counter(list2)
    return counts1 == counts2
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4]
    list_b = [2, 1, 4, 3, 2]
    list_c = [1, 2, 3, 4]
    list_d = [1, 2, 3, 5]
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")
    print(f"Comparing {list_a} and {list_d}: {compare_lists(list_a, list_d)}")