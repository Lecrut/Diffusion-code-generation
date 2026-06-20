def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return not a

if __name__ == '__main__':
    test_and = logical_and(True, False)
    test_or = logical_or(False, True)
    test_not = logical_not(True)
    print("AND:", test_and)
    print("OR:", test_or)
    print("NOT:", test_not)