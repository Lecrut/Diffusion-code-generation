def evaluate_gate(A: bool, B: bool, gate_type: str) -> bool:
    if gate_type == 'AND':
        return A and B
    elif gate_type == 'OR':
        return A or B
    elif gate_type == 'NOT':
        return not A
    else:
        raise ValueError("Invalid gate type")
if __name__ == '__main__':
    print(f"AND(True, True): {evaluate_gate(True, True, 'AND')}")
    print(f"AND(True, False): {evaluate_gate(True, False, 'AND')}")
    print(f"OR(True, False): {evaluate_gate(True, False, 'OR')}")
    print(f"OR(False, False): {evaluate_gate(False, False, 'OR')}")
    print(f"NOT(True): {evaluate_gate(True, False, 'NOT')}")
    print(f"NOT(False): {evaluate_gate(False, False, 'NOT')}")