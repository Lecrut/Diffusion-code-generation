def logical_or_lists(list_a, list_b):
    return [a or b for a, b in zip(list_a, list_b)]

if __name__ == '__main__':
    list_a = [True, False, True]
    list_b = [False, True, False]
    result = logical_or_lists(list_a, list_b)
    print(result)