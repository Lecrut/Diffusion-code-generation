def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Both inputs must be boolean values")
    return flag1 ^ flag2

if __name__ == '__main__':
    print(exclusive_truthiness(True, False))
    print(exclusive_truthiness(False, True))
    print(exclusive_truthiness(True, True))
    print(exclusive_truthiness(False, False))