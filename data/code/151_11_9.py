def validate_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    return list_a, list_b

def combine_lists_extend(list_a, list_b):
    list_a.extend(list_b)
    return list_a

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    try:
        combined_list = validate_lists(list1, list2)
        combined_list = combine_lists_extend(*combined_list)
        print(combined_list)
    except ValueError as e:
        print(e)