def logic_and(A, B):
    return A & B

def logic_or(A, B):
    return A | B

def logic_not(A):
    return ~A + 2

def logic_nand(A, B):
    return ~(A & B) + 2

def logic_nor(A, B):
    return ~(A | B) + 2

def logic_xor(A, B):
    return (A ^ B)

def logic_xnor(A, B):
    return ~(A ^ B) + 2

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"Inputs: A={A_val}, B={B_val}")
    print(f"AND: {logic_and(int(A_val), int(B_val))}")
    print(f"OR: {logic_or(int(A_val), int(B_val))}")
    print(f"NOT A: {logic_not(int(A_val))}")
    print(f"NAND: {logic_nand(int(A_val), int(B_val))}")
    print(f" NOR: {logic_nor(int(A_val), int(B_val))}")
    print(f"XOR: {logic_xor(int(A_val), int(B_val))}")
    print(f"XNOR: {logic_xnor(int(A_val), int(B_val))}")