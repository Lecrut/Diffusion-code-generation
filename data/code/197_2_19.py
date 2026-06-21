def find_common_elements(list1, list2):
    return set(list1) & set(list2)

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "David", "Eve"]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(f"Common elements: {common_elements}")