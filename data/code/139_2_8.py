def and_gate(A: bool, B: bool) -> bool:
    return A & B

def or_gate(A: bool, B: bool) -> bool:
    return A | B

def not_gate(A: bool) -> bool:
    return ~A + 1

def nand_gate(A: bool, B: bool) -> bool:
    return ~(A & B)

def nor_gate(A: bool, B: bool) -> bool:
    return ~(A | B)

def xor_gate(A: bool, B: bool) -> bool:
    return (A & ~B) | (~A & B)

def xnor_gate(A: bool, B: bool) -> bool:
    return ~(A ^ B)

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"AND({A_val}, {B_val}): {and_gate(A_val, B_val)}")
    print(f"OR({A_val}, {B_val}): {or_gate(A_val, B_val)}")
    print(f"NOT {A_val}: {not_gate(A_val)}")
    print(f"NAND({A_val}, {B_val}): {nand_gate(A_val, B_val)}")
    print(f"NOR({A_val}, {B_val}): {nor_gate(A_val, B_val)}")
    print(f"XOR({A_val}, {B_val}): {xor_gate(A_val, B_val)}")
    print(f"XNOR({A_val}, {B_val}): {xnor_gate(A_val, B_val)}")