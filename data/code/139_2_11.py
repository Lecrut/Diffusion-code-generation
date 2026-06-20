def and_gate(A, B):
    return A & B

def or_gate(A, B):
    return A | B

def not_gate(A):
    return ~A + 1

def nand_gate(A, B):
    return ~(A & B)

def nor_gate(A, B):
    return ~(A | B)

def xor_gate(A, B):
    return A ^ B

def xnor_gate(A, B):
    return ~(A ^ B)

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    
    print(f"AND: {and_gate(sample_A, sample_B)}")
    print(f"OR: {or_gate(sample_A, sample_B)}")
    print(f"NOT A: {not_gate(sample_A)}")
    print(f"NAND: {nand_gate(sample_A, sample_B)}")
    print(f"NOR: {nor_gate(sample_A, sample_B)}")
    print(f"XOR: {xor_gate(sample_A, sample_B)}")
    print(f"XNOR: {xnor_gate(sample_A, sample_B)}")