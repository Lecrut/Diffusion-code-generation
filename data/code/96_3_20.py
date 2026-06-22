def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if isinstance(expr, str):
        if expr.upper() == 'TRUE':
            return True
        if expr.upper() == 'FALSE':
            return False
        raise ValueError(f"Unsupported string value: {expr}")
    if not isinstance(expr, list) or len(expr) != 3:
        raise ValueError(f"Invalid expression structure: {expr}")
    left, op, right = expr
    left_val = evaluate_nested_expression(left)
    right_val = evaluate_nested_expression(right)
    if op == 'AND':
        return left_val and right_val
    if op == 'OR':
        return left_val or right_val
    if op == 'NOT':
        return not left_val
    raise ValueError(f"Unsupported operator: {op}")

if __name__ == '__main__':
    expression = [
        [
            [
                [True, 'AND', False],
                'OR',
                True
            ],
            'AND',
            False
        ]
    ]
    result = evaluate_nested_expression(expression)
    print(result)