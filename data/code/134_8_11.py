def count_and_check_exclusive(a, b, c, d, e):
    true_count = (a << 4) | (b << 3) | (c << 2) | (d << 1) | e
    return true_count == 0x10

if __name__ == '__main__':
    result = count_and_check_exclusive(True, False, True, False, True)
    print(result)