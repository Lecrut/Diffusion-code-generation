def logical_and(a: bool, b: bool) -> bool:
    return a & b

def logical_or(a: bool, b: bool) -> bool:
    return a | b

def logical_not(a: bool) -> bool:
    return not a

if __name__ == '__main__':
    sample_and = logical_and(True, False)
    sample_or = logical_or(False, True)
    sample_not = logical_not(True)
    
    print(sample_and)
    print(sample_or)
    print(sample_not)