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
        return bool(expr)
if __name__ == '__main__':
    expression = [[True, 'and', False], 'or', True]
    result = evaluate_expression(expression)
    print(result)