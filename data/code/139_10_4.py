def AND(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a & b

def OR(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a | b

def NOT(a):
    if not isinstance(a, bool):
        raise ValueError("Input must be a boolean value.")
    return ~a & 1

def XOR(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a ^ b

def NAND(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return ~(a & b)

def NOR(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return ~(a | b)

def XNOR(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return ~(a ^ b)

if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))
    print(NAND(True, True))
    print(NOR(False, False))
    print(XNOR(True, False))