def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both arguments must be boolean values.')
    return not a | b
if __name__ == '__main__':
    print(check_both_false(False, False))
    print(check_both_false(True, False))
    print(check_both_false(False, True))
    print(check_both_false(True, True))