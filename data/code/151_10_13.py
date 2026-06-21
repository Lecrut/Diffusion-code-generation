def validate_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in (list1, list2)):
        raise ValueError("Both inputs must be lists or tuples")
    return True

def concatenate_lists(list1, list2):
    validate_lists(list1, list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)