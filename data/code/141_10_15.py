def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return ~a + 1
if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_and(False, True))
    print(logical_or(True, False))
    print(logical_or(False, False))
    print(logical_not(True))
    print(logical_not(False))