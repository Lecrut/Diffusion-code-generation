def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return not a

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return not (a & b)

def NOR(a, b):
    return not (a | b)

def XNOR(a, b):
    return not (a ^ b)

if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))