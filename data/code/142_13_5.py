def compare_booleans(a: bool, b: bool) -> str:
    return "Identical" if a == b else "Different"

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))