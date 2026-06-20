def check_both_true(a: bool, b: bool) -> bool:
    return a & b

if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, False))
    print(check_both_true(True, False))
    print(check_both_true(False, True))