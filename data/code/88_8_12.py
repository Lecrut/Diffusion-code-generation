def check_both_true(a: bool, b: bool) -> bool:
    result = False
    if a is True and b is True:
        result = True
    return result
if __name__ == '__main__':
    print(check_both_true(True, True))
    print(check_both_true(False, True))
    print(check_both_true(True, False))
    print(check_both_true(False, False))