def check_conditions(a: bool, b: bool) -> bool:
    if a and not b:
        return True
    if not a and b:
        return True
    return False

if __name__ == '__main__':
    print(check_conditions(True, False))
    print(check_conditions(False, True))
    print(check_conditions(True, True))
    print(check_conditions(False, False))