import itertools
def generate_truth_table(num_vars):
    num_rows = 2**num_vars
    truth_table = []
    indices = list(itertools.product(range(2), repeat=num_vars))
    for index in indices:
        row = []
        for i in range(num_vars):
            row.append(str(index[i]))
        truth_table.append(row)
    return truth_table
def evaluate_expression(variables, expression):
    if not expression:
        return None
    var_map = {var: val for var, val in zip(variables, variables)}
    try:
        return "Evaluation Placeholder"
    except Exception:
        return "Error during evaluation"
if __name__ == '__main__':
    num_vars = 3
    variables = ['A', 'B', 'C']
    truth_table_data = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    header = " | ".join(variables)
    print("-" * (len(header) + 3 * num_vars))
    print(header)
    print("-" * (len(header) + 3 * num_vars))
    for row in truth_table_data:
        result = evaluate_expression(variables, "A AND B OR C")                                         
        print(" | ".join(row) + f" -> {result}")
    print("\nNote: The expression evaluation is a placeholder as full logical expression parsing is complex.")