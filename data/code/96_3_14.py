def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if not isinstance(expr, list):
        raise ValueError(f"Unsupported value: {expr}")
    if len(expr) == 0:
        raise ValueError("Empty expression list")
    if len(expr) == 1:
        return evaluate_nested_expression(expr[0])
    
    operator = expr[1]
    
    if operator == 'AND':
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[2])
        return left and right
    elif operator == 'OR':
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[2])
        return left or right
    elif operator == 'NOT':
        operand = evaluate_nested_expression(expr[0])
        return not operand
    else:
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    expression = [['AND', True, 'OR', ['AND', False, True]], 'OR', False]
    result = evaluate_nested_expression(expression)
    print(result)