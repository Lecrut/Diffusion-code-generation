def logical_and(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a and b

if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_and(True, False))
    print(logical_and(False, True))
    print(logical_and(False, False))