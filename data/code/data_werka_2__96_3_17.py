def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) < 3:
        raise ValueError("Invalid expression structure")
    op = expr[1]
    left = evaluate_nested_expression(expr[0])
    right = evaluate_nested_expression(expr[2])
    if op == 'and':
        return left and right
    elif op == 'or':
        return left or right
    elif op == 'not':
        return not left
    else:
        raise ValueError(f"Unsupported operator: {op}")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ['and', ['and', ['and', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)