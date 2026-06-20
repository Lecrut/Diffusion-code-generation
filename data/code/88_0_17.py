def check_both_true(a: bool, b: bool) -> bool:
    if not a:
        return False
    if not b:
        return False
    return True

if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, True))
    print(check_both_true(True, False))
    print(check_both_true(False, False))