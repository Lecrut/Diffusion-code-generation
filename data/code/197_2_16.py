def find_common_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return set(list1) & set(list2)

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "David", "Eve"]
    print(find_common_elements(sample_list1, sample_list2))