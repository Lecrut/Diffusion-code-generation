def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if not isinstance(expr, (list, tuple)):
        raise ValueError("Expected boolean or list")
    if len(expr) == 0:
        raise ValueError("Empty expression")
    if len(expr) == 1:
        return evaluate_nested_expression(expr[0])
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
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[1])
        return left and right
    raise ValueError("Unsupported expression structure")

if __name__ == '__main__':
    sample_expression = [
        [
            [True, 'or', False],
            'and',
            [
                [True, 'and', False],
                'or',
                True
            ]
        ],
        'and',
        False
    ]
    result = evaluate_nested_expression(sample_expression)
    print(result)