def and_gate(a: int, b: int) -> int:
    return a & b

def or_gate(a: int, b: int) -> int:
    return a | b

def not_gate(a: int) -> int:
    return 1 - a

def xor_gate(a: int, b: int) -> int:
    return a ^ b

def nand_gate(a: int, b: int) -> int:
    return not (a & b)

def nor_gate(a: int, b: int) -> int:
    return not (a | b)

def xnor_gate(a: int, b: int) -> int:
    return not (a ^ b)

if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    
    for a, b in inputs:
        print(f"AND({a}, {b}) = {and_gate(a, b)}")
        print(f"OR({a}, {b}) = {or_gate(a, b)}")
        print(f"NOT({a}) = {not_gate(a)}")
        print(f"XOR({a}, {b}) = {xor_gate(a, b)}")
        print(f"NAND({a}, {b}) = {nand_gate(a, b)}")
        print(f"NOR({a}, {b}) = {nor_gate(a, b)}")
        print(f"XNOR({a}, {b}) = {xnor_gate(a, b)}")