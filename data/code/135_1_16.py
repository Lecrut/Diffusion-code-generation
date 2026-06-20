def truth_table(expr1, expr2):
    import re
    from itertools import product
    vars = set(re.findall('[a-zA-Z]', expr1 + expr2))
    tables = list(product([True, False], repeat=len(vars)))

    def eval_expr(expr, table):
        return eval(expr, {'__builtins__': None}, {var: val for var, val in zip(vars, table)})
    return all((eval_expr(expr1, table) == eval_expr(expr2, table) for table in tables))
if __name__ == '__main__':
    expr1 = 'a and b'
    expr2 = 'b and a'
    print(truth_table(expr1, expr2))