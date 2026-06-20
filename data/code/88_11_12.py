def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not flag1 or not flag2:
        raise ValueError('At least one flag is false')
    return True

if __name__ == '__main__':
    sample_flag1 = False
    sample_flag2 = True
    try:
        result = validate_flags(sample_flag1, sample_flag2)
        print(result)
    except ValueError as e:
        print(e)