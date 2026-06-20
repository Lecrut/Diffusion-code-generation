from typing import Tuple

def and_logic(a: int, b: int) -> int:
    return a & b

def or_logic(a: int, b: int) -> int:
    return a | b

def not_logic(a: int) -> int:
    return 1 - a

def xor_logic(a: int, b: int) -> int:
    return (a | b) & ~(a & b)

def nand_logic(a: int, b: int) -> int:
    return not_logic(and_logic(a, b))

def nor_logic(a: int, b: int) -> int:
    return not_logic(or_logic(a, b))

def xnor_logic(a: int, b: int) -> int:
    return not_logic(xor_logic(a, b))

if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]

    for a, b in inputs:
        print(f"Inputs: A={a}, B={b}")
        print(f"AND: {and_logic(a, b)}")
        print(f"OR: {or_logic(a, b)}")
        print(f"NOT_A: {not_logic(a)}")
        print(f"NOT_B: {not_logic(b)}")
        print(f"XOR: {xor_logic(a, b)}")
        print(f"NAND: {nand_logic(a, b)}")
        print(f"NOR: {nor_logic(a, b)}")
        print(f"XNOR: {xnor_logic(a, b)}")