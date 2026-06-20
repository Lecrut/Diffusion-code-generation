def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("Input must be a boolean")
    return ~a + 1

if __name__ == '__main__':
    print(logical_and(True, False))
    print(logical_or(False, True))
    try:
        print(logical_not('a'))
    except ValueError as e:
        print(e)