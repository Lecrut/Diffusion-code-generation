TRUE = 1
FALSE = 0

def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return ~a + 1

if __name__ == '__main__':
    print(logical_and(TRUE, FALSE))
    print(logical_or(FALSE, TRUE))
    print(logical_not(TRUE))