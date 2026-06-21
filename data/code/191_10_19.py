def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def combine_lists(list1, list2):
    valid_list1, valid_list2 = validate_lists(list1, list2)
    result = valid_list1.copy()
    result.extend(valid_list2)
    return result

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    combined = combine_lists(list_a, list_b)
    print(combined)