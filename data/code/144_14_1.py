def evaluate_expression(expression, var1, var2):
    if "AND" in expression:
        return var1 and var2
    elif "OR" in expression:
        return var1 or var2
    elif "NOT" in expression:
        return not var1
    else:
        return False
def generate_truth_table(expr, v1_range, v2_range):
    results = []
    for v1 in v1_range:
        for v2 in v2_range:
            result = evaluate_expression(expr, v1, v2)
            results.append((v1, v2, result))
    return results
def print_truth_table(results):
    if not results:
        return
    header = "Variable 1 | Variable 2 | Expression Result"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for v1, v2, res in results:
        print(f"{v1:11} | {v2:11} | {res}")
    print("-" * len(header))
if __name__ == '__main__':
    expression = "V1 AND V2"
    v1_values = [0, 1]
    v2_values = [0, 1]
    truth_table_data = generate_truth_table(expression, v1_values, v2_values)
    print(f"Expression: {expression}\n")
    print_truth_table(truth_table_data)