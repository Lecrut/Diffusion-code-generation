def validate_flags(flag1, flag2):
    if not flag1 or not flag2:
        raise ValueError("At least one flag must be true")
    return True
if __name__ == '__main__':
    try:
        print(validate_flags(True, True))
        print(validate_flags(True, False))
        print(validate_flags(False, True))
        print(validate_flags(False, False))
    except ValueError as e:
        print(f"Caught an error: {e}")