def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not flag1 or not flag2:
        raise ValueError("At least one flag is False")
    return True

if __name__ == '__main__':
    try:
        print(validate_flags(True, True))
        print(validate_flags(False, True))
    except ValueError as e:
        print(e)