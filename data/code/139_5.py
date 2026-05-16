def create_truth_tables():
    truth_tables = {}
    and_table = {
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 1
    }
    truth_tables['AND'] = and_table
    or_table = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 1
    }
    truth_tables['OR'] = or_table
    not_table = {
        (0,): 1,
        (1,): 0
    }
    truth_tables['NOT'] = not_table
    xor_table = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    truth_tables['XOR'] = xor_table
    nand_table = {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    truth_tables['NAND'] = nand_table
    nor_table = {
        (0, 0): 1,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 0
    }
    truth_tables['NOR'] = nor_table
    return truth_tables
if __name__ == '__main__':
    truth_tables = create_truth_tables()
    print("Truth Tables:")
    for gate, table in truth_tables.items():
        print(f"\n--- {gate} ---")
        for inputs, output in table.items():
            print(f"Inputs: {inputs} -> Output: {output}")