def generate_truth_table(operator, a, b):
    results = {}
    if operator == 'and':
        results[(a, b)] = a and b
    elif operator == 'or':
        results[(a, b)] = a or b
    elif operator == 'not':
        results[(a, b)] = not a
    else:
        raise ValueError("Unsupported operator")
    return results
if __name__ == '__main__':
    operator_and = 'and'
    a_and = True
    b_and = False
    truth_table_and = generate_truth_table(operator_and, a_and, b_and)
    print(f"Truth Table for {operator_and} ({a_and}, {b_and}): {truth_table_and}")
    operator_or = 'or'
    a_or = True
    b_or = True
    truth_table_or = generate_truth_table(operator_or, a_or, b_or)
    print(f"Truth Table for {operator_or} ({a_or}, {b_or}): {truth_table_or}")
    operator_not = 'not'
    a_not = True
    b_not = False
    truth_table_not = generate_truth_table(operator_not, a_not, b_not)
    print(f"Truth Table for {operator_not} ({a_not}, {b_not}): {truth_table_not}")