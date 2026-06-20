def validate_flags(flag1, flag2):
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError('Both inputs must be boolean values')
    return flag1 and flag2
if __name__ == '__main__':
    try:
        print(validate_flags(True, True))
        print(validate_flags(True, False))
        print(validate_flags(False, True))
        print(validate_flags(False, False))
    except ValueError as e:
        print(f'Caught error: {e}')