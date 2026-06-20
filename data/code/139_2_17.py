def and_gate(A, B):
    return A & B

def or_gate(A, B):
    return A | B

def not_gate(A):
    return ~A + 2

def nand_gate(A, B):
    return ~(A & B) + 1

def nor_gate(A, B):
    return ~(A | B) + 1

def xor_gate(A, B):
    return (A & ~B) | (~A & B)

def xnor_gate(A, B):
    return ~(A ^ B) + 1

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"AND: {and_gate(int(A_val), int(B_val))}")
    print(f"OR: {or_gate(int(A_val), int(B_val))}")
    print(f"NOT A: {not_gate(int(A_val))}")
    print(f"NAND: {nand_gate(int(A_val), int(B_val))}")
    print(f"NOR: {nor_gate(int(A_val), int(B_val))}")
    print(f"XOR: {xor_gate(int(A_val), int(B_val))}")
    print(f"XNOR: {xnor_gate(int(A_val), int(B_val))}")