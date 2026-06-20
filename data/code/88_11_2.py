def validate_flags(flag1, flag2):
    if not flag1 or not flag2:
        raise ValueError('At least one flag is false')
    return True
if __name__ == '__main__':
    print(validate_flags(True, True))
    print(validate_flags(False, True))