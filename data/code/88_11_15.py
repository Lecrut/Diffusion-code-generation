VALIDATE_FLAGS_SUCCESS = True
VALIDATE_FLAGS_FAILURE = False

def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not flag1 or not flag2:
        raise ValueError('At least one flag is false')
    return VALIDATE_FLAGS_SUCCESS

if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(True, False))
    print(validate_flags(False, True))
    try:
        print(validate_flags(False, False))
    except ValueError as e:
        print(e)