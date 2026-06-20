def combine_flags(flag1: bool, flag2: bool) -> bool:
    return flag1 and flag2

if __name__ == '__main__':
    result = combine_flags(True, False)
    print(result)