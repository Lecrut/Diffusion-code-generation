import itertools
def find_common_unique(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4, 5]
    list_b = [3, 4, 5, 6, 7, 7]
    common = find_common_unique(list_a, list_b)
    print(common)