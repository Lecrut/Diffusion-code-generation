def evaluate_expression(expr):
    if isinstance(expr, list) and len(expr) == 3:
        left, op, right = expr
        if op == 'and':
            return evaluate_expression(left) and evaluate_expression(right)
        elif op == 'or':
            return evaluate_expression(left) or evaluate_expression(right)
    else:
        return expr

if __name__ == '__main__':
    sample_expr = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    print(evaluate_expression(sample_expr))