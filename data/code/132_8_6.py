COMBINE_FLAGS_MASK = 0xFFFFFFFF

def combine_flags(flag1: int, flag2: int) -> int:
    return flag1 | flag2 & COMBINE_FLAGS_MASK

if __name__ == '__main__':
    test_flag1 = 0b1010
    test_flag2 = 0b1100
    result = combine_flags(test_flag1, test_flag2)
    print(result)