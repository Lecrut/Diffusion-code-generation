def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(find_common_elements(sample_list1, sample_list2))