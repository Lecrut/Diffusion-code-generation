def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return 1 - a

def nand_gate(a, b):
    return 1 - (a & b)

def nor_gate(a, b):
    return 1 - (a | b)

def xor_gate(a, b):
    return a ^ b

def xnor_gate(a, b):
    return 1 - (a ^ b)

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    and_out = and_gate(input_a, input_b)
    or_out = or_gate(input_a, input_b)
    not_a_out = not_gate(input_a)
    not_b_out = not_gate(input_b)
    nand_out = nand_gate(input_a, input_b)
    nor_out = nor_gate(input_a, input_b)
    xor_out = xor_gate(input_a, input_b)
    xnor_out = xnor_gate(input_a, input_b)
    print("--- Results ---")
    print(f"AND ({input_a} AND {input_b}): {and_out}")
    print(f"OR ({input_a} OR {input_b}): {or_out}")
    print(f"NOT A (NOT {input_a}): {not_a_out}")
    print(f"NOT B (NOT {input_b}): {not_b_out}")
    print(f"NAND ({input_a} NAND {input_b}): {nand_out}")
    print(f"NOR ({input_a} NOR {input_b}): {nor_out}")
    print(f"XOR ({input_a} XOR {input_b}): {xor_out}")
    print(f"XNOR ({input_a} XNOR {input_b}): {xnor_out}")