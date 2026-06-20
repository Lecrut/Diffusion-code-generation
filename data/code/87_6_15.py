def validate_flags(flag1, flag2):
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Both inputs must be boolean flags.")
    return True

def combine_flags(flag1, flag2):
    if not validate_flags(flag1, flag2):
        return False
    return flag1 and flag2

if __name__ == '__main__':
    sample_flag1 = True
    sample_flag2 = False
    result = combine_flags(sample_flag1, sample_flag2)
    print(result)