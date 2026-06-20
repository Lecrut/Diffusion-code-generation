def truth_table(expr1, expr2):
    from itertools import product
    vars_expr1 = set(expr1.split() if ' ' in expr1 else [expr1])
    vars_expr2 = set(expr2.split() if ' ' in expr2 else [expr2])
    common_vars = vars_expr1.intersection(vars_expr2)
    truth_values = list(product([False, True], repeat=len(common_vars)))
    var_map = {var: values[i] for i, var in enumerate(common_vars)}
    results_expr1 = [eval(expr1, var_map) for _ in truth_values]
    results_expr2 = [eval(expr2, var_map) for _ in truth_values]
    return all((r1 == r2 for r1, r2 in zip(results_expr1, results_expr2)))
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = 'B and A'
    print(truth_table(expr1, expr2))