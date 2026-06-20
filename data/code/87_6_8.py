def combine_flags(flag1: bool, flag2: bool) -> bool:
    return flag1 and flag2

if __name__ == '__main__':
    sample_flag1 = True
    sample_flag2 = False
    result = combine_flags(sample_flag1, sample_flag2)
    print(result)