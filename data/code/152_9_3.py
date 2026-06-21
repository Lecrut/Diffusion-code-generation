def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50]
    sample_list_b = [40, 50, 60, 70, 80]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(common_elements)