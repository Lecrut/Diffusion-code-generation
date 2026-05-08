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
    return [1]                     
if __name__ == '__main__':
    num_vars = 3
    print(f"--- Truth Table Generation for {num_vars} Variables ---")
    truth_table_data = generate_truth_table(num_vars)
    print("\nVariable Assignments (Columns):")
    header = [f"V{i+1}" for i in range(num_vars)]
    print("| " + " | ".join(header) + " |")
    print("-" * (len(header) * 3 + 3 * (num_vars - 1)))
    for row in truth_table_data:
        print("| " + " | ".join(row) + " |")
    print("\nNote: The expression evaluation step is placeholder as full logical parsing is omitted.")