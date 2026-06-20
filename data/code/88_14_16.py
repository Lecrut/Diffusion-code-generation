def validate_flags(flag1, flag2):
    if not flag1:
        return False
    if not flag2:
        return False
    return True

if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(True, False))
    print(validate_flags(False, True))
    print(validate_flags(False, False))