def truth_table_and(a, b):
    return a and b
def truth_table_or(a, b):
    return a or b
def truth_table_not(a):
    return not a
def truth_table_xor(a, b):
    return a ^ b
def truth_table_nand(a, b):
    return not (a and b)
def truth_table_nor(a, b):
    return not (a or b)
def generate_truth_tables():
    results = {}
    def add_to_dict(name, inputs, outputs):
        key = tuple(inputs)
        results[name] = {key: outputs}
    add_to_dict("AND", [0, 0], [0])
    add_to_dict("AND", [0, 1], [0])
    add_to_dict("AND", [1, 0], [0])
    add_to_dict("AND", [1, 1], [1])
    add_to_dict("OR", [0, 0], [0])
    add_to_dict("OR", [0, 1], [1])
    add_to_dict("OR", [1, 0], [1])
    add_to_dict("OR", [1, 1], [1])
    add_to_dict("NOT", [0], [1])
    add_to_dict("NOT", [1], [0])
    add_to_dict("XOR", [0, 0], [0])
    add_to_dict("XOR", [0, 1], [1])
    add_to_dict("XOR", [1, 0], [1])
    add_to_dict("XOR", [1, 1], [0])
    add_to_dict("NAND", [0, 0], [1])
    add_to_dict("NAND", [0, 1], [1])
    add_to_dict("NAND", [1, 0], [1])
    add_to_dict("NAND", [1, 1], [0])
    add_to_dict("NOR", [0, 0], [1])
    add_to_dict("NOR", [0, 1], [0])
    add_to_dict("NOR", [1, 0], [0])
    add_to_dict("NOR", [1, 1], [0])
    return results
if __name__ == '__main__':
    truth_tables = generate_truth_tables()
    for gate, table in truth_tables.items():
        print(f"--- {gate} Truth Table ---")
        for inputs, outputs in table.items():
            print(f"Inputs: {list(inputs)}, Output: {list(outputs)}")
        print("\n")