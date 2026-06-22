def find_common_elements(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples.")
    
    return list(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 8]
    sample_list_2 = [-10, 5, 0, -20, 3]
    
    common_elements = find_common_elements(sample_list_1, sample_list_2)
    print(f"Common elements: {common_elements}")