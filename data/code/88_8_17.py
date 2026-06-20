def check_both_true(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    result1 = check_both_true(True, True)
    result2 = check_both_true(True, False)
    result3 = check_both_true(False, True)
    result4 = check_both_true(False, False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)