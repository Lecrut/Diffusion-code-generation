def compare_booleans(a: bool, b: bool) -> str:
    return 'Equal' if a == b else 'Not Equal'

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))
    print(compare_booleans(False, False))