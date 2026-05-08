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
    gates = {}
    gates['NOT'] = {
        (0,): 0,
        (1,): 1
    }
    gates['AND'] = {
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 1
    }
    gates['OR'] = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 1
    }
    gates['XOR'] = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    gates['NAND'] = {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    gates['NOR'] = {
        (0, 0): 1,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 0
    }
    return gates
if __name__ == '__main__':
    truth_tables = generate_truth_tables()
    print("Truth Tables:")
    for gate, table in truth_tables.items():
        print(f"\n{gate}:")
        for inputs, output in table.items():
            print(f"  Input: {inputs} -> Output: {output}")