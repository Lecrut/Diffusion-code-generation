VALIDATE_FALSE_ERROR = 'At least one flag is false'

def validate_flags(flag1, flag2):
    if not flag1 or not flag2:
        raise ValueError(VALIDATE_FALSE_ERROR)
    return True

if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(True, False))
    print(validate_flags(False, True))
    print(validate_flags(False, False))