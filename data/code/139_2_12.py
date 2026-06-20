def logic_and(A, B):
    return A & B

def logic_or(A, B):
    return A | B

def logic_not(A):
    return ~A + 2

def logic_nand(A, B):
    return ~(A & B) + 1

def logic_nor(A, B):
    return ~(A | B) + 1

def logic_xor(A, B):
    return A ^ B

def logic_xnor(A, B):
    return ~(A ^ B) + 1

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    
    and_res = logic_and(sample_A, sample_B)
    or_res = logic_or(sample_A, sample_B)
    not_A_val = logic_not(sample_A)
    nand_res = logic_nand(sample_A, sample_B)
    nor_res = logic_nor(sample_A, sample_B)
    xor_res = logic_xor(sample_A, sample_B)
    xnor_res = logic_xnor(sample_A, sample_B)

    print(f"Inputs: A={sample_A}, B={sample_B}")
    print(f"AND: {and_res}")
    print(f"OR: {or_res}")
    print(f"NOT A: {not_A_val}")
    print(f"NAND: {nand_res}")
    print(f"NOR: {nor_res}")
    print(f"XOR: {xor_res}")
    print(f"XNOR: {xnor_res}")