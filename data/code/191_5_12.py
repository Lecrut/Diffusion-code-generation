def validate_lists(list_a, list_b):
    if not all(isinstance(item, bool) for item in list_a + list_b):
        raise ValueError("Both lists must contain only boolean values")

def combine_lists(list_a, list_b):
    validate_lists(list_a, list_b)
    return [a or b for a, b in zip(list_a, list_b)]

if __name__ == '__main__':
    list_a = [True, False, True]
    list_b = [False, True, False]
    combined_list = combine_lists(list_a, list_b)
    print(combined_list)