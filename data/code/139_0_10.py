def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a & 1

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return ~(a & b)

def NOR(a, b):
    return ~(a | b)

def XNOR(a, b):
    return ~(a ^ b)
if __name__ == '__main__':
    print(AND(True, True))
    print(OR(False, False))
    print(NOT(True))
    print(XOR(True, False))
    print(NAND(True, False))
    print(NOR(False, True))
    print(XNOR(False, False))