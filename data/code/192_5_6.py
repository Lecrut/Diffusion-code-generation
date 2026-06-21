def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(common_elements)