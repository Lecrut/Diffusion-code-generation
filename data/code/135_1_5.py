def truth_table(expr1: str, expr2: str) -> bool:
    import itertools
    vars_expr1 = set(expr1.split() if ' ' in expr1 else [expr1])
    vars_expr2 = set(expr2.split() if ' ' in expr2 else [expr2])
    common_vars = vars_expr1.intersection(vars_expr2)
    truth_assignments = list(itertools.product([False, True], repeat=len(common_vars)))
    for assignment in truth_assignments:
        eval_dict = dict(zip(common_vars, assignment))
        if eval(expr1, eval_dict) != eval(expr2, eval_dict):
            return False
    return True
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = 'B and A'
    print(truth_table(expr1, expr2))