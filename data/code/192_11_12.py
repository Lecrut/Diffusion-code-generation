def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a & set_b)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 6, 7, 8, 5]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)