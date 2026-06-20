def count_and_check_exclusive(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
    count = int(a) + int(b) + int(c) + int(d) + int(e)
    return count == 1

if __name__ == '__main__':
    result = count_and_check_exclusive(True, False, True, False, False)
    print(result)