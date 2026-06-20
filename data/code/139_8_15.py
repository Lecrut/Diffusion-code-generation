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
    print("--- Logic Gate Demonstrations ---")
    a_and = 0
    b_and = 0
    print(f"AND(0, 0) = {AND(a_and, b_and)}")
    
    a_or = 0
    b_or = 1
    print(f"OR(0, 1) = {OR(a_or, b_or)}")
    
    a_not = 1
    print(f"NOT(1) = {NOT(a_not)}")
    
    a_xor = 1
    b_xor = 0
    print(f"XOR(1, 0) = {XOR(a_xor, b_xor)}")
    
    a_nand = 1
    b_nand = 1
    print(f"NAND(1, 1) = {NAND(a_nand, b_nand)}")
    
    a_nor = 0
    b_nor = 1
    print(f"NOR(0, 1) = {NOR(a_nor, b_nor)}")
    
    a_xnor = 1
    b_xnor = 1
    print(f"XNOR(1, 1) = {XNOR(a_xnor, b_xnor)}")