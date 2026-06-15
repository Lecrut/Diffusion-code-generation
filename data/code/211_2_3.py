import collections
def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    symmetric_diff_set = set1.symmetric_difference(set2)
    return sorted(list(symmetric_diff_set))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = symmetric_difference(list_a, list_b)
    print(result)