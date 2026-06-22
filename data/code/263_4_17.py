def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 8]
    sample_list_2 = [-10, 5, 0, -20, 3]
    common_elements = find_common_elements(sample_list_1, sample_list_2)
    print(f"List 1: {sample_list_1}")
    print(f"List 2: {sample_list_2}")
    print(f"Common elements: {common_elements}")