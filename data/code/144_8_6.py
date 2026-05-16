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
    return [int(v) for v in variables]
if __name__ == '__main__':
    num_vars = 3
    print(f"--- Truth Table Generation for {num_vars} Variables ---")
    truth_table_data = generate_truth_table(num_vars)
    header = list(range(num_vars))
    header_names = [f'V{i}' for i in header]
    print("Variables | Expression Evaluation")
    print("-" * 30)
    for row in truth_table_data:
        variable_values = [f'{v}' for v in row]
        evaluation_result = "N/A (Requires Parser)"
        print(f"{' | '.join(header_names)} | {evaluation_result}")
    print("\n--- Detailed Truth Table (Input Rows) ---")
    for row in truth_table_data:
        print(row)