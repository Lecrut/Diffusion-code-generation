def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) == 3:
        left = evaluate_nested_expression(expr[0])
        op = expr[1]
        right = evaluate_nested_expression(expr[2])
        if op == 'and':
            return left and right
        elif op == 'or':
            return left or right
        elif op == 'not':
            return not left
        else:
            raise ValueError(f"Unsupported operator: {op}")
    if len(expr) == 2:
        op = expr[0]
        operand = expr[1]
        val = evaluate_nested_expression(operand)
        if op == 'not':
            return not val
        else:
            raise ValueError(f"Unsupported unary operator: {op}")
    raise ValueError(f"Invalid expression structure: {expr}")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ['or', ['and', ['and', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)