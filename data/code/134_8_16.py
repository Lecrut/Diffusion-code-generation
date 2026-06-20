def count_and_check_exclusive(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
    return a + b + c + d + e == 1
if __name__ == '__main__':
    print(count_and_check_exclusive(True, False, False, False, False))
    print(count_and_check_exclusive(False, True, False, False, False))
    print(count_and_check_exclusive(False, False, True, False, False))
    print(count_and_check_exclusive(False, False, False, True, False))
    print(count_and_check_exclusive(False, False, False, False, True))
    print(count_and_check_exclusive(True, True, False, False, False))