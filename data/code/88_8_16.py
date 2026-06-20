def check_both_true(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("First argument must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("Second argument must be a boolean")
    return a and b

if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, True))
    print(check_both_true(True, False))
    print(check_both_true(False, False))