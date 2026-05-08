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
    results['AND'] = {
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 1
    }
    results['OR'] = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 1
    }
    results['NOT'] = {
        (0,): 1,
        (1,): 0
    }
    results['XOR'] = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    results['NAND'] = {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    results['NOR'] = {
        (0, 0): 1,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 0
    }
    return results
if __name__ == '__main__':
    truth_tables = generate_truth_tables()
    print("Truth Tables:")
    for gate, table in truth_tables.items():
        print(f"\n{gate}:")
        for input_tuple, output in table.items():
            print(f"Input: {input_tuple} -> Output: {output}")