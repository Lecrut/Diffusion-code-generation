def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not (flag1 and flag2):
        raise ValueError('At least one flag is false')
    return True

if __name__ == '__main__':
    sample_flag1 = True
    sample_flag2 = False
    result = validate_flags(sample_flag1, sample_flag2)
    print(result)