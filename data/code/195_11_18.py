def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return True

def intersect_lists(list1, list2):
    validate_lists(list1, list2)
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8]
    print(intersect_lists(sample_list1, sample_list2))