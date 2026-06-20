def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')
    return not a and (not b)
if __name__ == '__main__':
    try:
        print(check_both_false(False, False))
        print(check_both_false(True, False))
        print(check_both_false(False, True))
        print(check_both_false(True, True))
    except ValueError as e:
        print(e)