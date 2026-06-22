def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4]
    sample_list_b = [3, 4, 5, 6]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(f"Common elements between {sample_list_a} and {sample_list_b}: {common_elements}")