def validate_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")
    return list1, list2

def join_lists(list1, list2):
    list1, list2 = validate_lists(list1, list2)
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    result = join_lists(sample_list1, sample_list2)
    print(result)