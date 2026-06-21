def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    count = count_common_elements(sample_list_a, sample_list_b)
    print(f"Number of common elements: {count}")