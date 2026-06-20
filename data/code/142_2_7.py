def compare_booleans(flag1: bool, flag2: bool) -> bool:
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Inputs must be boolean values")
    return flag1 == flag2

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))