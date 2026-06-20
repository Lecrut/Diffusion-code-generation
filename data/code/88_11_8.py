def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not flag1 or not flag2:
        raise ValueError('At least one flag is false')
    return True

if __name__ == '__main__':
    result1 = validate_flags(True, True)
    result2 = validate_flags(True, False)
    print(result1)
    print(result2)