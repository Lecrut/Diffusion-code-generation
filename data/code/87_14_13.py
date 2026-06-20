def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    return flag1 ^ flag2

if __name__ == '__main__':
    sample1 = exclusive_truthiness(True, False)
    sample2 = exclusive_truthiness(False, True)
    sample3 = exclusive_truthiness(True, True)
    sample4 = exclusive_truthiness(False, False)

    print(f"Sample 1 (True, False): {sample1}")
    print(f"Sample 2 (False, True): {sample2}")
    print(f"Sample 3 (True, True): {sample3}")
    print(f"Sample 4 (False, False): {sample4}")