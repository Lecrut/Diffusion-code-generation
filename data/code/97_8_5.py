import itertools
def generate_truth_table(num_variables):
    num_rows = 2 ** num_variables
    truth_table = []
    variable_names = [f'V{i+1}' for i in range(num_variables)]
    for i in range(num_rows):
        values = []
        for j in range(num_variables):
            bit = (i >> j) & 1
            values.append(str(bit))
        truth_table.append(values)
    return truth_table, variable_names
if __name__ == '__main__':
    num_vars = 3
    truth_table, names = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    print(" | ".join(names))
    print("-" * (len(names) * 3 + (len(names) - 1)))
    for row in truth_table:
        print(" | ".join(row))