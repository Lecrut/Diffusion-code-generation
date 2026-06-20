def count_and_check_exclusive(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
    count = (a << 4) | (b << 3) | (c << 2) | (d << 1) | e
    return count & (count - 1) == 0

if __name__ == '__main__':
    result = count_and_check_exclusive(True, False, True, False, False)
    print(result)