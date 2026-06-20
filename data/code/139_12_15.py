def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

def NAND(a, b):
    return 1 - (a & b)

def NOR(a, b):
    return 1 - (a | b)

def XOR(a, b):
    return a ^ b

def XNOR(a, b):
    return ~(a ^ b) & 1

if __name__ == '__main__':
    input_a = 0
    input_b = 1
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    and_out = AND(input_a, input_b)
    or_out = OR(input_a, input_b)
    not_a = NOT(input_a)
    not_b = NOT(input_b)
    nand_out = NAND(input_a, input_b)
    nor_out = NOR(input_a, input_b)
    xor_out = XOR(input_a, input_b)
    xnor_out = XNOR(input_a, input_b)
    print(f"AND result: {and_out}")
    print(f"OR result: {or_out}")
    print(f"NOT A result: {not_a}")
    print(f"NOT B result: {not_b}")
    print(f"NAND result: {nand_out}")
    print(f"NOR result: {nor_out}")
    print(f"XOR result: {xor_out}")
    print(f"XNOR result: {xnor_out}")