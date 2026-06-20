def truth_table(expr1: str, expr2: str) -> bool:
    import itertools

    def evaluate(expression: str, values: dict) -> bool:
        for var in expression.split():
            if var.isalpha() and var not in values:
                return False
        return eval(expression, {}, values)
    vars_expr1 = set((var for var in expr1.split() if var.isalpha()))
    vars_expr2 = set((var for var in expr2.split() if var.isalpha()))
    common_vars = vars_expr1.intersection(vars_expr2)
    if not common_vars:
        return False
    for combination in itertools.product([False, True], repeat=len(common_vars)):
        values = dict(zip(common_vars, combination))
        if evaluate(expr1, values) != evaluate(expr2, values):
            return False
    return True
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = 'B and A'
    print(truth_table(expr1, expr2))