def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(False, True)
    print(result2)
    result3 = check_both_false(True, False)
    print(result3)
    result4 = check_both_false(True, True)
    print(result4)