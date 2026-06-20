import numpy as np

GATE_DICT = {
    'AND': np.logical_and,
    'OR': np.logical_or,
    'NOT': np.logical_not
}

def apply_gate(gate_name, *arrays):
    gate_func = GATE_DICT.get(gate_name)
    if gate_func is None:
        raise ValueError(f"Unknown gate: {gate_name}")
    return gate_func(*arrays)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("AND:", apply_gate('AND', a, b))
    print("OR:", apply_gate('OR', a, b))
    print("NOT A:", apply_gate('NOT', a))