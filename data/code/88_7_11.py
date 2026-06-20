def both_true(a: bool, b: bool) -> str:
    return "Both are true" if a and b else "At least one is false"

if __name__ == '__main__':
    print(both_true(True, True))
    print(both_true(False, True))
    print(both_true(True, False))
    print(both_true(False, False))