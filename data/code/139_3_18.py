def and_gate(a: int, b: int) -> int:
    return a & b

def or_gate(a: int, b: int) -> int:
    return a | b

def not_a_gate(a: int) -> int:
    return 1 - a

def not_b_gate(b: int) -> int:
    return 1 - b

def nand_gate(a: int, b: int) -> int:
    return 1 - (a & b)

def nor_gate(a: int, b: int) -> int:
    return 1 - (a | b)

def xnor_gate(a: int, b: int) -> int:
    return (a & b) ^ (b & a)

if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    for a, b in inputs:
        print(f"AND({a}, {b}):", and_gate(a, b))
        print(f"OR({a}, {b}):", or_gate(a, b))
        print(f"NOT_A({a}):", not_a_gate(a))
        print(f"NOT_B({b}):", not_b_gate(b))
        print(f"NAND({a}, {b}):", nand_gate(a, b))
        print(f"NOR({a}, {b}):", nor_gate(a, b))
        print(f"XNOR({a}, {b}):", xnor_gate(a, b))