def check_or_condition(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    return a or b

if __name__ == '__main__':
    print(check_or_condition(True, False))
    print(check_or_condition(False, True))
    print(check_or_condition(True, True))
    print(check_or_condition(False, False))