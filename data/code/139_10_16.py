def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return not a

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return not a & b

def NOR(a, b):
    return not a | b

def XNOR(a, b):
    return not a ^ b
if __name__ == '__main__':
    result_and = AND(True, False)
    result_or = OR(False, True)
    result_not = NOT(True)
    result_xor = XOR(True, True)
    result_nand = NAND(True, True)
    result_nor = NOR(False, False)
    result_xnor = XNOR(True, False)
    print('AND:', result_and)
    print('OR:', result_or)
    print('NOT:', result_not)
    print('XOR:', result_xor)
    print('NAND:', result_nand)
    print('NOR:', result_nor)
    print('XNOR:', result_xnor)