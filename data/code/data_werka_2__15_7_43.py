def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        return False

def are_lists_identical(list1, list2):
    validation_result = validate_lists(list1, list2)
    if validation_result is False:
        return False
    for elem1, elem2 in zip(list1, list2):
        if elem1 != elem2:
            return False
    return True

if __name__ == '__main__':
    sample_list1 = [100, 200, 300, 400, 500]
    sample_list2 = [100, 200, 300, 400, 500]
    sample_list3 = [100, 200, 300, 400, 600]
    print(are_lists_identical(sample_list1, sample_list2))
    print(are_lists_identical(sample_list1, sample_list3))