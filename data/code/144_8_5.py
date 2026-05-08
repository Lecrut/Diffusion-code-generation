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
    pass
if __name__ == '__main__':
    num_vars = 3
    print(f"Variables: {num_vars}")
    truth_table = generate_truth_table(num_vars)
    header = list(range(num_vars))
    header_names = [f'V{i+1}' for i in header]
    print("--------------------------------------------------")
    print("Truth Table")
    print("--------------------------------------------------")
    header_line = " | ".join(header_names)
    print(f"| {header_line} |")
    print("-" * (len(header_line) + 3 * num_vars + 1))
    for row in truth_table:
        row_values = [str(x) for x in row]
        print("| " + " | ".join(row_values) + " |")