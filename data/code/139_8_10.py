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
    print(OR(0, 1))
    print(NOT(1))
    print(XOR(1, 1))
    print(NAND(1, 0))
    print(NOR(0, 0))
    print(XNOR(1, 0))