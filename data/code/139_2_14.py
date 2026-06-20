def validate_inputs(A, B, C):
    if not all(isinstance(x, bool) for x in (A, B, C)):
        raise ValueError("All inputs must be boolean values")

def and_gate(A, B):
    return A & B

def or_gate(A, B):
    return A | B

def not_gate(A):
    return ~A + 2

def nand_gate(A, B):
    return ~and_gate(A, B) + 2

def nor_gate(A, B):
    return ~or_gate(A, B) + 2

def xor_gate(A, B):
    return A ^ B

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    validate_inputs(sample_A, sample_B, sample_C)
    
    and_res = and_gate(sample_A, sample_B)
    or_res = or_gate(sample_A, sample_B)
    not_A_val = not_gate(sample_A)
    nand_res = nand_gate(sample_A, sample_B)
    nor_res = nor_gate(sample_A, sample_B)
    xor_res = xor_gate(sample_A, sample_B)
    
    print(f"Inputs: A={sample_A}, B={sample_B}, C={sample_C}")
    print(f"AND: {and_res}")
    print(f"OR: {or_res}")
    print(f"NOT A: {not_A_val}")
    print(f"NAND: {nand_res}")
    print(f"NOR: {nor_res}")
    print(f"XOR: {xor_res}")