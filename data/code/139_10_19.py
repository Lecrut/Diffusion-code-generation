def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a + 2

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return ~(a & b) + 2

def NOR(a, b):
    return ~(a | b) + 2

def XNOR(a, b):
    return ~(a ^ b) + 2
if __name__ == '__main__':
    print(AND(True, True))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, False))
    print(NAND(True, False))
    print(NOR(False, False))
    print(XNOR(True, True))