def check_booleans(a: bool, b: bool) -> str:
    return "Both are true" if a and b else "At least one is false"

if __name__ == '__main__':
    print(check_booleans(True, True))
    print(check_booleans(False, False))