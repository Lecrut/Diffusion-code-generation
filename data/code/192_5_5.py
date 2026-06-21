def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60]
    sample_list2 = [30, 40, 50, 60, 70, 80]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)