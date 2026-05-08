def evaluate_gate(A, B, gate_type):
    if gate_type == 'AND':
        return A and B
    elif gate_type == 'OR':
        return A or B
    elif gate_type == 'NOT':
        return not A
    else:
        raise ValueError("Invalid gate type")
if __name__ == '__main__':
    A_val = True
    B_val = False
    result_and = evaluate_gate(A_val, B_val, 'AND')
    result_or = evaluate_gate(A_val, B_val, 'OR')
    result_not = evaluate_gate(A_val, B_val, 'NOT')
    print(f"A={A_val}, B={B_val}, AND: {result_and}")
    print(f"A={A_val}, B={B_val}, OR: {result_or}")
    print(f"A={A_val}, B={B_val}, NOT: {result_not}")