TRUE = True

def check_both_true(a: bool, b: bool) -> bool:
    return a == TRUE and b == TRUE
if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, True))
    print(check_both_true(True, False))
    print(check_both_true(False, False))