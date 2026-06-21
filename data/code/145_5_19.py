def de_morgan_optimize(expr):
    if isinstance(expr, tuple) and len(expr) == 3:
        op = expr[0]
        a, b = expr[1], expr[2]
        if op == 'and':
            return ('or', de_morgan_optimize(('not', a)), de_morgan_optimize(('not', b)))
        elif op == 'or':
            return ('and', de_morgan_optimize(('not', a)), de_morgan_optimize(('not', b)))
    return expr

def evaluate(expr):
    if isinstance(expr, tuple) and len(expr) == 3:
        op = expr[0]
        a, b = expr[1], expr[2]
        if op == 'and':
            return evaluate(a) and evaluate(b)
        elif op == 'or':
            return evaluate(a) or evaluate(b)
    elif isinstance(expr, bool):
        return expr
    else:
        raise ValueError("Invalid expression")

if __name__ == '__main__':
    sample_expr = ('and', ('not', True), ('or', False, True))
    optimized_expr = de_morgan_optimize(sample_expr)
    print(optimized_expr)
    print(evaluate(optimized_expr))