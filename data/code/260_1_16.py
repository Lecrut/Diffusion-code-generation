def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list_a = [1, 3, 5, 7, 9]
    sample_list_b = [0, 2, 4, 6, 8, 7, 9]
    common_result = find_common_elements(sample_list_a, sample_list_b)
    print(common_result)