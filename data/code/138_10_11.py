def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b

if __name__ == '__main__':
    print("AND(True, True):", AND(True, True))
    print("AND(True, False):", AND(True, False))
    print("AND(False, True):", AND(False, True))
    print("AND(False, False):", AND(False, False))

    print("OR(True, True):", OR(True, True))
    print("OR(True, False):", OR(True, False))
    print("OR(False, True):", OR(False, True))
    print("OR(False, False):", OR(False, False))

    print("NOT(True):", NOT(True))
    print("NOT(False):", NOT(False))

    print("NAND(True, True):", NAND(True, True))
    print("NAND(True, False):", NAND(True, False))
    print("NAND(False, True):", NAND(False, True))
    print("NAND(False, False):", NAND(False, False))

    print("NOR(True, True):", NOR(True, True))
    print("NOR(True, False):", NOR(True, False))
    print("NOR(False, True):", NOR(False, True))
    print("NOR(False, False):", NOR(False, False))

    print("XOR(True, True):", XOR(True, True))
    print("XOR(True, False):", XOR(True, False))
    print("XOR(False, True):", XOR(False, True))
    print("XOR(False, False):", XOR(False, False))

    print("XNOR(True, True):", XNOR(True, True))
    print("XNOR(True, False):", XNOR(True, False))
    print("XNOR(False, True):", XNOR(False, True))
    print("XNOR(False, False):", XNOR(False, False))