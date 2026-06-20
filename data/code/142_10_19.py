def are_booleans_equal(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values')
    not_a = not a
    not_b = not b
    return not_a and not_b or (a and b)
if __name__ == '__main__':
    try:
        print(are_booleans_equal(True, True))
        print(are_booleans_equal(False, False))
        print(are_booleans_equal(True, False))
    except ValueError as e:
        print(e)