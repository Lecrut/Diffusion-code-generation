def is_both_false(x, y):
    if not isinstance(x, bool) or not isinstance(y, bool):
        raise ValueError('Both inputs must be boolean values.')
    return not x and (not y)
if __name__ == '__main__':
    print(is_both_false(False, False))
    print(is_both_false(True, False))
    print(is_both_false(False, True))
    print(is_both_false(True, True))