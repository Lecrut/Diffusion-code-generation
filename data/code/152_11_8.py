def find_common_elements(list1, list2):
    set2 = set(list2)
    common_items = [item for item in list1 if item in set2]
    return common_items

if __name__ == '__main__':
    sample_list_a = [1, 2, 2, 3, 4, 4]
    sample_list_b = [2, 4, 4, 5, 6, 1]
    result = find_common_elements(sample_list_a, sample_list_b)
    print(result)