def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'Different'
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))