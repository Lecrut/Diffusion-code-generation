def check_booleans(a: bool, b: bool) -> str:
    if not a or not b:
        return "At least one value is False"
    return "Both values are True"

if __name__ == '__main__':
    print(check_booleans(True, True))
    print(check_booleans(False, True))
    print(check_booleans(True, False))
    print(check_booleans(False, False))