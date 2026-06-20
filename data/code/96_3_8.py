def evaluate_expression(expr):
    if isinstance(expr, list) and len(expr) == 3:
        left = evaluate_expression(expr[0])
        operator = expr[1]
        right = evaluate_expression(expr[2])
        if operator == 'and':
            return left and right
        elif operator == 'or':
            return left or right
    else:
        raise ValueError("Invalid expression")

if __name__ == '__main__':
    sample_expr = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = evaluate_expression(sample_expr)
    print(result)