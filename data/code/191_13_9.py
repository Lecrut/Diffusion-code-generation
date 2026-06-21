def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def combine_lists(list1, list2):
    list1, list2 = validate_lists(list1, list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    combined = combine_lists(sample_list1, sample_list2)
    print(combined)