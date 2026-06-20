def validate_flags(flag1, flag2):
    if not (flag1 or flag2):
        raise ValueError('At least one flag must be True')
    return True
if __name__ == '__main__':
    print(validate_flags(True, False))
    print(validate_flags(False, False))