def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "Charlie", "David"]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(f"Common elements: {common_elements}")