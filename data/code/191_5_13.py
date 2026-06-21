def logical_or_lists(list_a, list_b):
    return [x or y for x, y in zip(list_a, list_b)]

if __name__ == '__main__':
    sample_list_a = [True, False, True]
    sample_list_b = [False, True, False]
    result = logical_or_lists(sample_list_a, sample_list_b)
    print(result)