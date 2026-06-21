def is_valid_list(lst):
    return isinstance(lst, list)

def intersect_lists(list1, list2):
    if not (is_valid_list(list1) and is_valid_list(list2)):
        raise ValueError("Both inputs must be lists.")
    
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8]
    print(intersect_lists(sample_list1, sample_list2))