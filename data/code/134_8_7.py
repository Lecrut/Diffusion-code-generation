def count_and_check_exclusive(a, b, c, d, e):
    return bool(a + b + c + d + e & 1)
if __name__ == '__main__':
    print(count_and_check_exclusive(True, False, True, False, False))
    print(count_and_check_exclusive(False, False, False, False, False))
    print(count_and_check_exclusive(True, True, True, True, True))