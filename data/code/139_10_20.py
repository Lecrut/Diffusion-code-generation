TRUE = True
FALSE = False

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return not a

def XOR(a, b):
    return a & ~b | ~a & b

def NAND(a, b):
    return ~(a & b)

def NOR(a, b):
    return ~(a | b)

def XNOR(a, b):
    return ~(a ^ b)
if __name__ == '__main__':
    print(AND(TRUE, FALSE))
    print(OR(FALSE, TRUE))
    print(NOT(TRUE))