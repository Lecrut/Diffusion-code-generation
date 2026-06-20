def truth_table(expr1: str, expr2: str) -> bool:
    from itertools import product
    vars_set = set(expr1).union(set(expr2))
    vars_list = sorted(vars_set)
    truth_assignments = list(product([False, True], repeat=len(vars_list)))
    for assignment in truth_assignments:
        eval_expr1 = eval(expr1, {var: assign for var, assign in zip(vars_list, assignment)})
        eval_expr2 = eval(expr2, {var: assign for var, assign in zip(vars_list, assignment)})
        if eval_expr1 != eval_expr2:
            return False
    return True
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = 'B and A'
    print(truth_table(expr1, expr2))