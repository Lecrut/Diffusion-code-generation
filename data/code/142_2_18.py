def compare_booleans(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    result_ab = compare_booleans(sample_a, sample_b)
    print(result_ab)