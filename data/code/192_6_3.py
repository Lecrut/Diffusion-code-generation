import itertools
def find_common_unique(list1, list2):
    unique1 = set(list1)
    unique2 = set(list2)
    common_elements = unique1.intersection(unique2)
    return list(common_elements)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    result = find_common_unique(list_a, list_b)
    print(result)