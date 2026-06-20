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
    print("--- Gate Demonstrations ---")
    a = 0
    b = 0
    print(f"AND(0, 0) = {AND(a, b)}")
    print(f"OR(0, 0) = {OR(a, b)}")
    print(f"NOT(0) = {NOT(a)}")
    print(f"XOR(0, 0) = {XOR(a, b)}")
    print(f"NAND(0, 0) = {NAND(a, b)}")
    print(f"NOR(0, 0) = {NOR(a, b)}")
    print(f"XNOR(0, 0) = {XNOR(a, b)}")

    a = 1
    b = 0
    print(f"AND(1, 0) = {AND(a, b)}")
    print(f"OR(1, 0) = {OR(a, b)}")
    print(f"NOT(1) = {NOT(a)}")
    print(f"XOR(1, 0) = {XOR(a, b)}")
    print(f"NAND(1, 0) = {NAND(a, b)}")
    print(f"NOR(1, 0) = {NOR(a, b)}")
    print(f"XNOR(1, 0) = {XNOR(a, b)}")

    a = 0
    b = 1
    print(f"AND(0, 1) = {AND(a, b)}")
    print(f"OR(0, 1) = {OR(a, b)}")
    print(f"NOT(0) = {NOT(a)}")
    print(f"XOR(0, 1) = {XOR(a, b)}")
    print(f"NAND(0, 1) = {NAND(a, b)}")
    print(f"NOR(0, 1) = {NOR(a, b)}")
    print(f"XNOR(0, 1) = {XNOR(a, b)}")

    a = 1
    b = 1
    print(f"AND(1, 1) = {AND(a, b)}")
    print(f"OR(1, 1) = {OR(a, b)}")
    print(f"NOT(1) = {NOT(a)}")
    print(f"XOR(1, 1) = {XOR(a, b)}")
    print(f"NAND(1, 1) = {NAND(a, b)}")
    print(f"NOR(1, 1) = {NOR(a, b)}")
    print(f"XNOR(1, 1) = {XNOR(a, b)}")