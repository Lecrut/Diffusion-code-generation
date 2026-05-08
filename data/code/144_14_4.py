def evaluate_expression(expression, var1, var2):
    if "AND" in expression:
        return var1 and var2
    elif "OR" in expression:
        return var1 or var2
    elif "NOT" in expression:
        return not var1
    else:
        return var1 == var2
def generate_truth_table(expression, val1_range, val2_range):
    results = []
    for v1 in val1_range:
        for v2 in val2_range:
            result = evaluate_expression(expression, v1, v2)
            results.append((v1, v2, result))
    return results
if __name__ == '__main__':
    expression = "NOT (Var1 AND Var2)"
    values1 = [0, 1]
    values2 = [0, 1]
    truth_table = generate_truth_table(expression, values1, values2)
    print("Truth Table for Expression:")
    print("--------------------------")
    print(f"{'Var1':<5} | {'Var2':<5} | {'Result':<6}")
    print("--------------------------")
    for v1, v2, result in truth_table:
        print(f"{v1:<5} | {v2:<5} | {result:<6}")