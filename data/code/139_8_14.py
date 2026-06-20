def AND(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return a & b

def OR(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return a | b

def NOT(a):
    if not isinstance(a, int):
        raise ValueError("Input must be an integer")
    return ~a + 2

def XOR(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return a ^ b

def NAND(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return ~(a & b) + 2

def NOR(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return ~(a | b) + 2

def XNOR(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return ~(a ^ b) + 2

if __name__ == '__main__':
    print("--- Gate Demonstrations ---")
    print(f"AND(0, 0) = {AND(0, 0)}")
    print(f"AND(0, 1) = {AND(0, 1)}")
    print(f"AND(1, 0) = {AND(1, 0)}")
    print(f"OR(0, 0) = {OR(0, 0)}")
    print(f"OR(0, 1) = {OR(0, 1)}")
    print(f"OR(1, 0) = {OR(1, 0)}")
    print(f"NOT(0) = {NOT(0)}")
    print(f"NOT(1) = {NOT(1)}")
    print(f"XOR(0, 0) = {XOR(0, 0)}")
    print(f"XOR(0, 1) = {XOR(0, 1)}")
    print(f"XOR(1, 0) = {XOR(1, 0)}")
    print(f"NAND(0, 0) = {NAND(0, 0)}")
    print(f"NAND(0, 1) = {NAND(0, 1)}")
    print(f"NAND(1, 0) = {NAND(1, 0)}")
    print(f"NOR(0, 0) = {NOR(0, 0)}")
    print(f"NOR(0, 1) = {NOR(0, 1)}")
    print(f"NOR(1, 0) = {NOR(1, 0)}")
    print(f"XNOR(0, 0) = {XNOR(0, 0)}")
    print(f"XNOR(0, 1) = {XNOR(0, 1)}")
    print(f"XNOR(1, 0) = {XNOR(1, 0)}")