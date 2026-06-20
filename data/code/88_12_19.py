def check_both_true(a: bool, b: bool) -> bool:
    TRUE = 1
    FALSE = 0
    return (a << 1) | b == TRUE

if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, True))
    print(check_both_true(True, False))
    print(check_both_true(False, False))