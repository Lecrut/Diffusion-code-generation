def validate_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    return list_a, list_b

def append_in_place(list_a, list_b):
    for item in list_b:
        list_a.append(item)
    return list_a

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    valid_list_a, valid_list_b = validate_lists(sample_list_a, sample_list_b)
    result = append_in_place(valid_list_a, valid_list_b)
    print(result)