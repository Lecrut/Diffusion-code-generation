import sys
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)
if __name__ == '__main__':
    list_a = [1, 5, 2, 8, 3, 9, 4, 7]
    list_b = [8, 3, 1, 9, 10, 2, 6, 5]
    common_elements = find_common_elements(list_a, list_b)
    print(common_elements)