def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b

if __name__ == '__main__':
    A = [True, True, False, False]
    B = [True, False, True, False]

    print("A | B | AND | OR | NOT | NAND | NOR | XOR | XNOR")
    print("---|---|-----|----|-----|------|-----|-----|-------")
    for a, b in zip(A, B):
        and_result = AND(a, b)
        or_result = OR(a, b)
        not_a = NOT(a)
        nand_result = NAND(a, b)
        nor_result = NOR(a, b)
        xor_result = XOR(a, b)
        xnor_result = XNOR(a, b)
        print(f"{a} | {b} | {and_result} | {or_result} | {not_a} | {nand_result} | {nor_result} | {xor_result} | {xnor_result}")