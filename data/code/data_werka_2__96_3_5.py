def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) != 3:
        raise ValueError("Invalid expression structure")
    op = expr[1]
    left = evaluate_nested_expression(expr[0])
    right = evaluate_nested_expression(expr[2])
    if op == 'AND':
        return left and right
    if op == 'OR':
        return left or right
    if op == 'NOT':
        return not left
    raise ValueError(f"Unsupported operator: {op}")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ['AND', ['AND', ['AND', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)