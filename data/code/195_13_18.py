def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if any(not isinstance(item, (int, float, str)) for item in list1 + list2):
        raise ValueError("Lists can only contain integers, floats, and strings.")

def set_difference(list1, list2):
    validate_lists(list1, list2)
    diff = []
    for item in list1:
        if all(item != other_item for other_item in list2):
            diff.append(item)
    return diff

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = set_difference(sample_list1, sample_list2)
    print(result)