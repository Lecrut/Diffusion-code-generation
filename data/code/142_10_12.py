def are_booleans_equal(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values')
    return (not a) == (not b)
if __name__ == '__main__':
    try:
        print(are_booleans_equal(True, True))
        print(are_booleans_equal(False, False))
        print(are_booleans_equal(True, False))
        print(are_booleans_equal(False, True))
        print(are_booleans_equal('True', True))
    except ValueError as e:
        print(e)