LOGICAL_TRUE = 1
LOGICAL_FALSE = 0

def logical_and(a: bool, b: bool) -> bool:
    return bool(LOGICAL_TRUE & (a << 1 | b))

def logical_or(a: bool, b: bool) -> bool:
    return bool(LOGICAL_TRUE | (a << 1 | b))

def logical_not(a: bool) -> bool:
    return not a

if __name__ == '__main__':
    print(logical_and(True, False))
    print(logical_or(False, True))
    print(logical_not(True))