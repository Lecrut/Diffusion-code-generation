import itertools
def generate_truth_table(num_vars):
    num_rows = 2**num_vars
    truth_table = []
    indices = range(num_rows)
    for i in indices:
        row = []
        for j in range(num_vars):
            bit = (i >> j) & 1
            row.append(str(bit))
        truth_table.append(row)
    return truth_table
def evaluate_expression(variables, expression):
    if not expression:
        return None
    return expression
if __name__ == '__main__':
    num_vars = 3
    truth_table_data = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    header = list(range(num_vars))
    header_names = [f"V{i+1}" for i in header]
    print(" | ".join(header_names))
    print("-" * (len(header_names) * 3 + 1))
    for row in truth_table_data:
        row_output = []
        for var_value in row:
            row_output.append(var_value)
        print(" | ".join(row_output))
    print("\nNote: The expression evaluation step is omitted as it requires a complex expression parser not implemented here.")