def validate_lists(list_a, list_b):
    if not all(isinstance(item, bool) for item in list_a):
        raise ValueError("list_a must contain only booleans")
    if not all(isinstance(item, bool) for item in list_b):
        raise ValueError("list_b must contain only booleans")

def combine_bool_lists(list_a, list_b):
    validate_lists(list_a, list_b)
    return [x or y for x, y in zip_longest(list_a, list_b, fillvalue=False)]

if __name__ == '__main__':
    list_a = [True, False, True]
    list_b = [False, True, False]
    combined_list = combine_bool_lists(list_a, list_b)
    print(combined_list)