def count_and_check_exclusive(a, b, c, d, e):
    count = (a + b + c + d + e) & 1
    return bool(count)

if __name__ == '__main__':
    print(count_and_check_exclusive(True, False, True, False, False))