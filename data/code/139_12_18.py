def AND_GATE(a, b):
    return a & b

def OR_GATE(a, b):
    return a | b

def NOT_GATE(x):
    return 1 - x

def XOR_GATE(x, y):
    return x ^ y

def NAND_GATE(x, y):
    return AND_GATE(x, y) ^ 1

def NOR_GATE(x, y):
    return OR_GATE(x, y) ^ 1

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    and_out = AND_GATE(input_a, input_b)
    or_out = OR_GATE(input_a, input_b)
    not_a_out = NOT_GATE(input_a)
    not_b_out = NOT_GATE(input_b)
    xor_out = XOR_GATE(input_a, input_b)
    nand_out = NAND_GATE(input_a, input_b)
    nor_out = NOR_GATE(input_a, input_b)
    print("--- Results ---")
    print(f"AND ({input_a} AND {input_b}): {and_out}")
    print(f"OR ({input_a} OR {input_b}): {or_out}")
    print(f"NOT A (NOT {input_a}): {not_a_out}")
    print(f"NOT B (NOT {input_b}): {not_b_out}")
    print(f"XOR ({input_a} XOR {input_b}): {xor_out}")
    print(f"NAND ({input_a} NAND {input_b}): {nand_out}")
    print(f"NOR ({input_a} NOR {input_b}): {nor_out}")