def check_both_false(a: bool, b: bool) -> bool:
    if a:
        return False
    if b:
        return False
    return True

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)
    result3 = check_both_false(False, True)
    print(result3)
    result4 = check_both_false(True, True)
    print(result4)