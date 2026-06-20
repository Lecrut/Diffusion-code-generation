def check_exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    return flag1 ^ flag2

if __name__ == '__main__':
    result = check_exclusive_truthiness(True, False)
    print(result)