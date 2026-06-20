def compare_booleans(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2
if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result1 = compare_booleans(sample1, sample1)
    result2 = compare_booleans(sample2, sample2)
    result3 = compare_booleans(sample1, sample2)
    print(result1)
    print(result2)
    print(result3)