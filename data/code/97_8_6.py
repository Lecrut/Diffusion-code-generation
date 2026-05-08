def generate_truth_table(num_variables):
    num_rows = 2 ** num_variables
    header = [f"V{i}" for i in range(num_variables)]
    table = []
    for i in range(num_rows):
        row_values = []
        binary_representation = bin(i)[2:].zfill(num_variables)
        for j in range(num_variables):
            value = int(binary_representation[j])
            row_values.append(str(value))
        table.append(row_values)
    return header, table
if __name__ == '__main__':
    num_vars = 3
    header, table = generate_truth_table(num_vars)
    print("--- Truth Table for", num_vars, "Variables ---")
    print("Variables: " + " | ".join(header))
    print("-" * 30)
    for row in table:
        print(" | ".join(row))