def generate_truth_table(num_vars):
    if num_vars <= 0:
        return "Number of variables must be positive."
    num_rows = 2**num_vars
    truth_table = []
    for i in range(num_rows):
        row_values = []
        for j in range(num_vars):
            bit = (i >> j) & 1
            row_values.append(str(bit))
        truth_table.append(row_values)
    return truth_table

def evaluate_expression(variables, expression):
    if not expression:
        return None
    a, b, c, d = map(int, variables)
    if expression == "(A OR B) AND (C OR D)":
        return (a or b) and (c or d)
    return None

if __name__ == '__main__':
    num_vars = 4
    truth_table_data = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    headers = [f"V{i+1}" for i in range(num_vars)]
    print(" | ".join(headers))
    for row in truth_table_data:
        print(" | ".join(row))

    sample_combination = ['0', '1', '1', '0']
    result = evaluate_expression(sample_combination, "(A OR B) AND (C OR D)")
    print(f"Result for {sample_combination}: {result}")