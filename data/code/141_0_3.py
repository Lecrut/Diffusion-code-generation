def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return ~a + 1 == 0
if __name__ == '__main__':
    print(logical_and(True, False))
    print(logical_or(False, True))
    print(logical_not(True))