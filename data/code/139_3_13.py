def and_(a: bool, b: bool) -> bool:
    return a & b

def or_(a: bool, b: bool) -> bool:
    return a | b

def not_(a: bool) -> bool:
    return ~a & 1

def xor_(a: bool, b: bool) -> bool:
    return (a ^ b) & 1

def nand_(a: bool, b: bool) -> bool:
    return ~(a & b) & 1

def nor_(a: bool, b: bool) -> bool:
    return ~(a | b) & 1

def xnor_(a: bool, b: bool) -> bool:
    return (a == b) & 1
if __name__ == '__main__':
    print(and_(True, False))
    print(or_(True, False))
    print(not_(True))
    print(xor_(True, False))
    print(nand_(True, False))
    print(nor_(True, False))
    print(xnor_(True, False))