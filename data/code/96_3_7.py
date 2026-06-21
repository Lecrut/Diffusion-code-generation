def evaluate_boolean_expression(expr):
    if isinstance(expr, bool):
        return expr
    if not isinstance(expr, list):
        raise ValueError("Unsupported input type")
    if len(expr) == 0:
        raise ValueError("Empty expression")
    if len(expr) == 1:
        return evaluate_boolean_expression(expr[0])
    if len(expr) == 2:
        left = evaluate_boolean_expression(expr[0])
        right = evaluate_boolean_expression(expr[1])
        return left and right
    if len(expr) == 3:
        left = evaluate_boolean_expression(expr[0])
        op = expr[1]
        right = evaluate_boolean_expression(expr[2])
        if op == 'AND':
            return left and right
        elif op == 'OR':
            return left or right
        elif op == 'XOR':
            return left ^ right
        elif op == 'NAND':
            return not (left and right)
        elif op == 'NOR':
            return not (left or right)
        else:
            raise ValueError(f"Unsupported operator: {op}")
    raise ValueError("Unsupported expression length")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ((A, 'AND', B), 'OR', (C, 'AND', D))
    result = evaluate_boolean_expression(expr)
    print(result)