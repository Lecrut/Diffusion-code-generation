def check_booleans(a: bool, b: bool) -> str:
    if a and b:
        return "Both are true"
    else:
        return "At least one is false"

if __name__ == '__main__':
    print(check_booleans(True, True))
    print(check_booleans(False, True))
    print(check_booleans(True, False))
    print(check_booleans(False, False))