def validate_input(list1, list2):
    if not all(isinstance(item, tuple) for item in list1 + list2):
        raise ValueError("Both inputs must be lists of tuples")
    return True

def extend_tuples(list1, list2):
    validate_input(list1, list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(5, 6), (7, 8)]
    result = extend_tuples(sample_list1, sample_list2)
    print(result)