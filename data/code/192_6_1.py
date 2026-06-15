import numpy as np
def find_common_elements(list1, list2):
    unique_list1 = set(list1)
    unique_list2 = set(list2)
    common_elements = unique_list1.intersection(unique_list2)
    return list(common_elements)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(list_a, list_b)
    print(result)