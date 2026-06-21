def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) < 3:
        raise ValueError("Invalid expression structure")
    op = expr[1]
    left = evaluate_nested_expression(expr[0])
    if len(expr) == 3:
        right = evaluate_nested_expression(expr[2])
    else:
        right = evaluate_nested_expression([expr[2], op, expr[3:]])
    if op == 'AND':
        return left and right
    elif op == 'OR':
        return left or right
    elif op == 'XOR':
        return left ^ right
    else:
        raise ValueError(f"Unsupported operator: {op}")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = [
        [
            [
                [A, 'AND', B],
                'OR',
                C
            ],
            'AND',
            D
        ]
    ]
    result = evaluate_nested_expression(expr)
    print(result)