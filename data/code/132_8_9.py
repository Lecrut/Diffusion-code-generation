FLAG_MASK = 255

def combine_flags(flag1: int, flag2: int) -> int:
    return flag1 | flag2 & FLAG_MASK
if __name__ == '__main__':
    test_flag1 = 170
    test_flag2 = 85
    result = combine_flags(test_flag1, test_flag2)
    print(result)