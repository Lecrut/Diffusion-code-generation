def check_both_false(bool1: bool, bool2: bool) -> bool:
    return not bool1 and not bool2

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)