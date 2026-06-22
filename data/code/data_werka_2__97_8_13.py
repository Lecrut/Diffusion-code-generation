def compute_logic_table(val_a, val_b):
    if not isinstance(val_a, bool) or not isinstance(val_b, bool):
        raise ValueError("Inputs must be boolean values")
    ops = {
        "AND": lambda x, y: x and y,
        "OR": lambda x, y: x or y,
        "XOR": lambda x, y: x != y,
        "NAND": lambda x, y: not (x and y),
        "NOR": lambda x, y: not (x or y),
        "IMPLIES_A_TO_B": lambda x, y: (not x) or y,
        "IMPLIES_B_TO_A": lambda x, y: (not y) or x,
        "EQUALITY": lambda x, y: x == y,
    }
    table = {
        "input_a": val_a,
        "input_b": val_b,
    }
    for name, op in ops.items():
        table[name] = op(val_a, val_b)
    return table

if __name__ == '__main__':
    result = compute_logic_table(True, False)
    print(result)