def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    result1 = check_boolean_equality(True, True)
    result2 = check_boolean_equality(False, False)
    result3 = check_boolean_equality(True, False)
    print(result1)
    print(result2)
    print(result3)