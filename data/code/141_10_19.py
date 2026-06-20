def logical_and(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a | b

def logical_not(a: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("Input must be a boolean value.")
    return ~a + 1

if __name__ == '__main__':
    print(logical_and(True, False))
    print(logical_or(False, True))
    print(logical_not(True))