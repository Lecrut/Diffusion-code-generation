def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) == 3:
        left = evaluate_nested_expression(expr[0])
        op = expr[1]
        right = evaluate_nested_expression(expr[2])
        if op == 'AND':
            return left and right
        elif op == 'OR':
            return left or right
        elif op == 'NOT':
            return not left
        else:
            raise ValueError(f"Unsupported operator: {op}")
    if len(expr) == 2:
        op = expr[0]
        operand = evaluate_nested_expression(expr[1])
        if op == 'NOT':
            return not operand
        else:
            raise ValueError(f"Unsupported unary operator: {op}")
    raise ValueError("Invalid expression structure")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ['AND', ['AND', ['AND', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)