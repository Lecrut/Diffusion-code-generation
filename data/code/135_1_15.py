def truth_table(expr1, expr2):
    from itertools import product

    def evaluate(expr, values):
        for var, value in values.items():
            expr = expr.replace(var, str(value))
        return eval(expr)

    vars_expr1 = set(expr1.split()) & {'True', 'False'}
    vars_expr2 = set(expr2.split()) & {'True', 'False'}

    if vars_expr1 != vars_expr2:
        return False

    for values in product([True, False], repeat=len(vars_expr1)):
        if evaluate(expr1, dict(zip(vars_expr1, values))) != evaluate(expr2, dict(zip(vars_expr1, values))):
            return False
    return True

if __name__ == '__main__':
    expr1 = "A and B"
    expr2 = "B and A"
    print(truth_table(expr1, expr2))