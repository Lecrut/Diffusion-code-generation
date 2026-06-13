import sys
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)
if __name__ == '__main__':
    list_a = [1, 5, 3, 7, 9, 10, 11, 15]
    list_b = [10, 3, 8, 15, 2, 11, 4]
    common_elements = find_common_elements(list_a, list_b)
    print(common_elements)