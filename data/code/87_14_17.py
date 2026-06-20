def exclusive_truthiness(flag_a: bool, flag_b: bool) -> bool:
    return flag_a ^ flag_b

if __name__ == '__main__':
    result = exclusive_truthiness(True, False)
    print(result)