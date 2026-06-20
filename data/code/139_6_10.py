GATE_AND = 0
GATE_OR = 1
GATE_NOT = 2
GATE_XOR = 3

def apply_gate(a, b=None, gate_type=GATE_AND):
    if gate_type == GATE_AND:
        return a & b
    elif gate_type == GATE_OR:
        return a | b
    elif gate_type == GATE_NOT:
        return ~a
    elif gate_type == GATE_XOR:
        return a ^ b
    else:
        raise ValueError('Invalid gate type')
if __name__ == '__main__':
    print(apply_gate(1, 0, GATE_AND))
    print(apply_gate(1, 0, GATE_OR))
    print(apply_gate(1, None, GATE_NOT))
    print(apply_gate(1, 0, GATE_XOR))