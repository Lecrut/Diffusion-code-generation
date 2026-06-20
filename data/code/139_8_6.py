def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a + 2

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return ~(a & b) + 1

def NOR(a, b):
    return ~(a | b) + 1

def XNOR(a, b):
    return ~(a ^ b) + 1
if __name__ == '__main__':
    print(AND(0, 0))
    print(OR(0, 0))
    print(NOT(0))
    print(XOR(0, 0))
    print(NAND(0, 0))
    print(NOR(0, 0))
    print(XNOR(0, 0))