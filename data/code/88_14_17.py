def validate_flags(flag1, flag2):
    return flag1 and flag2

if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(True, False))
    print(validate_flags(False, True))
    print(validate_flags(False, False))