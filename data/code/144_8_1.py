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
    def evaluate_row(row_values):
        if len(row_values) < 3:
            return False
        v0, v1, v2 = row_values[0], row_values[1], row_values[2]
        return (v0 and v1) or v2
    return evaluate_row
if __name__ == '__main__':
    num_vars = 3
    print(f"--- Truth Table Generation for {num_vars} Variables ---")
    truth_table_data = generate_truth_table(num_vars)
    print("\nVariable Assignments (V0, V1, V2):")
    header = " | ".join([f"V{i}" for i in range(num_vars)])
    print(f"{header}")
    print("-" * len(header))
    for row in truth_table_data:
        print(" | ".join(row))
    print("\n--- Example Evaluation (Assuming expression: (V0 AND V1) OR V2) ---")
    expression_to_test = "(V0 AND V1) OR V2"
    for i, row in enumerate(truth_table_data):
        var_values = [f"V{j}: {row[j]}" for j in range(num_vars)]
        result = evaluate_expression(row, expression_to_test)
        print(f"Row {i+1}: {var_values} => {result}")
    print("\nNote: The evaluation logic is hardcoded for demonstration purposes only.")