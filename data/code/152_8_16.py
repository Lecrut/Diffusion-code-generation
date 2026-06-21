def find_intersection(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples.")
    
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    intersection_result = find_intersection(sample_list1, sample_list2)
    print(intersection_result)