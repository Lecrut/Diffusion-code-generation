def combine_booleans(list_a, list_b):
    if not all(isinstance(item, bool) for item in list_a + list_b):
        raise ValueError("Both lists must contain only boolean values.")
    return [x or y for x, y in zip(list_a, list_b)]

if __name__ == '__main__':
    try:
        list_a = [True, False, True]
        list_b = [False, True, False]
        combined_list = combine_booleans(list_a, list_b)
        print(combined_list)
    except ValueError as e:
        print(e)