def AND(a: bool, b: bool) -> bool:
    return a & b

def OR(a: bool, b: bool) -> bool:
    return a | b

def NOT(a: bool) -> bool:
    return not a

def XOR(a: bool, b: bool) -> bool:
    return a ^ b

def NAND(a: bool, b: bool) -> bool:
    return not a & b

def NOR(a: bool, b: bool) -> bool:
    return not a | b

def XNOR(a: bool, b: bool) -> bool:
    return not a ^ b
if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))
    print(NAND(True, True))
    print(NOR(False, False))
    print(XNOR(True, False))