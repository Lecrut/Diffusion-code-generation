def evaluate_expression(expr, var1, var2, var3):
    if "AND" in expr:
        return var1 and var2
    elif "OR" in expr:
        return var1 or var2
    elif "NOT" in expr:
        return not var3

def generate_truth_table():
    results = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = evaluate_expression("(A AND B) OR (NOT C)", a, b, c)
                results.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)