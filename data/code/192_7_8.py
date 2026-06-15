import sys
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)
if __name__ == '__main__':
    list_a = [1, 5, 2, 8, 3, 9, 4, 5]
    list_b = [5, 8, 1, 9, 10, 3, 7]
    result = find_common_elements(list_a, list_b)
    print(result)