def check_validity(val1: bool, val2: bool) -> None:
    if not isinstance(val1, bool) or not isinstance(val2, bool):
        raise ValueError("Both inputs must be boolean values.")

def logical_and(a: bool, b: bool) -> bool:
    check_validity(a, b)
    return a and b

if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_and(True, False))
    print(logical_and(False, True))
    print(logical_and(False, False))