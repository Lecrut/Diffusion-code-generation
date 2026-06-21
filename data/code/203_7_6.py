def compare_booleans(a: bool, b: bool) -> int:
    return int(a != b)

if __name__ == '__main__':
    result = compare_booleans(False, True)
    print(result)