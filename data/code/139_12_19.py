def and_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return a & b

def or_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return a | b

def not_gate(a: int) -> int:
    if not a in {0, 1}:
        raise ValueError("Input must be binary (0 or 1)")
    return 1 - a

def nand_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return 1 - (a & b)

def nor_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return 1 - (a | b)

def xor_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return a ^ b

def xnor_gate(a: int, b: int) -> int:
    if not (a in {0, 1} and b in {0, 1}):
        raise ValueError("Inputs must be binary (0 or 1)")
    return 1 - (a ^ b)

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print("--- Results ---")
    print(f"AND ({input_a} AND {input_b}): {and_gate(input_a, input_b)}")
    print(f"OR ({input_a} OR {input_b}): {or_gate(input_a, input_b)}")
    print(f"NOT A (NOT {input_a}): {not_gate(input_a)}")