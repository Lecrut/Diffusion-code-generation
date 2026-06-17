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
    list_b = [3, 2, 1, 4, 2]
    list_c = [1, 2, 3, 4]
    list_d = [1, 2, 3, 4, 5]
    list_e = [1, 2, 2, 3, 5]
    print(f"List A: {list_a}, List B: {list_b} -> Same elements/frequencies: {compare_lists(list_a, list_b)}")
    print(f"List A: {list_a}, List C: {list_c} -> Same elements/frequencies: {compare_lists(list_a, list_c)}")
    print(f"List D: {list_d}, List E: {list_e} -> Same elements/frequencies: {compare_lists(list_d, list_e)}")