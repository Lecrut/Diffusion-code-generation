def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    print(check_boolean_equality(sample1, sample2))
    print(check_boolean_equality(False, False))