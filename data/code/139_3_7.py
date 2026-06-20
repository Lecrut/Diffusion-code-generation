def and_(a: bool, b: bool) -> bool:
    return a & b

def or_(a: bool, b: bool) -> bool:
    return a | b

def not_(a: bool) -> bool:
    return ~a + 1

def xor(a: bool, b: bool) -> bool:
    return a & ~b | ~a & b

def nand(a: bool, b: bool) -> bool:
    return ~(a & b) + 1

def nor(a: bool, b: bool) -> bool:
    return ~(a | b) + 1

def xnor(a: bool, b: bool) -> bool:
    return ~(a ^ b) + 1
if __name__ == '__main__':
    print(and_(True, False))
    print(or_(True, False))
    print(not_(True))
    print(xor(True, False))
    print(nand(True, False))
    print(nor(True, False))
    print(xnor(True, False))