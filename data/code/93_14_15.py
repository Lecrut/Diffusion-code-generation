def check_both_false(a: bool, b: bool) -> bool:
    FALSE = False
    return a == FALSE and b == FALSE

if __name__ == '__main__':
    print(check_both_false(False, False))
    print(check_both_false(True, False))
    print(check_both_false(False, True))
    print(check_both_false(True, True))