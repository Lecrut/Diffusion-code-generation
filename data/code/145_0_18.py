def check_nested_conditions(a: bool, b: bool, c: bool) -> bool:
    return (a and b) or (c and not b)

if __name__ == '__main__':
    print(check_nested_conditions(True, False, True))
    print(check_nested_conditions(False, False, False))
    print(check_nested_conditions(True, True, True))