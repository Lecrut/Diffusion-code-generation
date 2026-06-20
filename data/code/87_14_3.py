def exclusive_truthiness(flag_a: bool, flag_b: bool) -> bool:
    return flag_a ^ flag_b

if __name__ == '__main__':
    print(exclusive_truthiness(True, False))
    print(exclusive_truthiness(False, True))
    print(exclusive_truthiness(True, True))
    print(exclusive_truthiness(False, False))