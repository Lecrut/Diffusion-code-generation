def generate_truth_table(num_variables):
    num_rows = 2 ** num_variables
    table = []
    for i in range(num_rows):
        row = []
        for j in range(num_variables):
            bit = (i >> j) & 1
            row.append(str(bit))
        table.append(row)
    return table
if __name__ == '__main__':
    num_vars = 3
    truth_table = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    header = " | ".join([f"V{i+1}" for i in range(num_vars)])
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for row in truth_table:
        print(" | ".join(row))