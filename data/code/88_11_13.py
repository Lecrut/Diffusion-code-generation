def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not flag1:
        raise ValueError('Flag 1 is false')
    if not flag2:
        raise ValueError('Flag 2 is false')
    return True

if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(True, False))
    print(validate_flags(False, True))
    print(validate_flags(False, False))