def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def append_elements(target_list, elements_to_add):
    target_list += elements_to_add

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    
    valid_list1, valid_list2 = validate_lists(sample_list1, sample_list2)
    append_elements(valid_list1, valid_list2)
    
    print("Updated List 1:", valid_list1)