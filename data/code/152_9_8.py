def find_shared_elements(list_a, list_b):
    if not all(isinstance(item, (list, tuple)) for item in [list_a, list_b]):
        raise ValueError("Both inputs must be lists or tuples.")
    
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.intersection(set_b)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    shared_elements = find_shared_elements(sample_list1, sample_list2)
    print(shared_elements)