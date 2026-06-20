def check_exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    return flag1 ^ flag2
if __name__ == '__main__':
    print(check_exclusive_truthiness(True, False))
    print(check_exclusive_truthiness(False, True))
    print(check_exclusive_truthiness(True, True))
    print(check_exclusive_truthiness(False, False))