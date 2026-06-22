from itertools import product

OPERATIONS = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x != y,
    "NAND": lambda x, y: not (x and y),
    "NOR": lambda x, y: not (x or y),
    "IMPLIES_A_TO_B": lambda x, y: (not x) or y,
    "IMPLIES_B_TO_A": lambda x, y: (not y) or x,
    "EQUALITY": lambda x, y: x == y,
}

def generate_truth_table(boolean_a, boolean_b):
    if not isinstance(boolean_a, bool) or not isinstance(boolean_b, bool):
        raise ValueError("Inputs must be boolean values")
    table = {
        "input_a": boolean_a,
        "input_b": boolean_b,
    }
    for name, op in OPERATIONS.items():
        table[name] = op(boolean_a, boolean_b)
    return table

if __name__ == '__main__':
    result = generate_truth_table(True, False)
    print(result)