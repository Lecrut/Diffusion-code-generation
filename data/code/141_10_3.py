def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return not a
if __name__ == '__main__':
    result_and = logical_and(True, False)
    result_or = logical_or(False, True)
    result_not = logical_not(True)
    print(result_and)
    print(result_or)
    print(result_not)