def check_both_false(a: bool, b: bool) -> bool:
    return not (a or b)
if __name__ == '__main__':
    print(check_both_false(False, False))
    print(check_both_false(True, False))
    print(check_both_false(False, True))
    print(check_both_false(True, True))