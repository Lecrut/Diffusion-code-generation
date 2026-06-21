def combine_lists(list_a, list_b):
    if not all((isinstance(item, bool) for item in list_a + list_b)):
        raise ValueError('Both lists must contain only boolean values')
    return [x or y for x, y in zip_longest(list_a, list_b, fillvalue=False)]
if __name__ == '__main__':
    list_a = [True, False, True]
    list_b = [False, True, False]
    combined_result = combine_lists(list_a, list_b)
    print(combined_result)