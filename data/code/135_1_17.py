def truth_table(expr1: str, expr2: str) -> bool:
    from itertools import product
    vars_expr1 = set(expr1.replace(' ', '').replace('!', ''))
    vars_expr2 = set(expr2.replace(' ', '').replace('!', ''))
    common_vars = vars_expr1.intersection(vars_expr2)
    truth_values = list(product([True, False], repeat=len(common_vars)))
    for vals in truth_values:
        env = dict(zip(common_vars, vals))
        eval1 = eval(expr1, env)
        eval2 = eval(expr2, env)
        if eval1 != eval2:
            return False
    return True
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = 'B and A'
    print(truth_table(expr1, expr2))