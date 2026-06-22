def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 8]
    sample_list2 = [-10, 5, 0, -20, 3]
    common_vals = find_common_elements(sample_list1, sample_list2)
    print(f"List 1: {sample_list1}")
    print(f"List 2: {sample_list2}")
    print(f"Common elements: {common_vals}")