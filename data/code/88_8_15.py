def check_both_true(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')
    return a and b
if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, False))
    try:
        print(check_both_true(1, True))
    except ValueError as e:
        print(e)