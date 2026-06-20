def logical_and(val1: bool, val2: bool) -> bool:
    if not isinstance(val1, bool) or not isinstance(val2, bool):
        raise ValueError("Both inputs must be boolean values.")
    return val1 and val2

if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_and(True, False))
    print(logical_and(False, True))
    print(logical_and(False, False))