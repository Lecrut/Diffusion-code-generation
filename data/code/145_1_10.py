def evaluate_nested_logic(expression):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, dict):
        operator = next(iter(expression.keys()))
        operands = expression.values()
        if operator == 'and':
            return all(evaluate_nested_logic(op) for op in operands)
        elif operator == 'or':
            return any(evaluate_nested_logic(op) for op in operands)
        elif operator == 'not':
            return not evaluate_nested_logic(operands[0])
    else:
        raise ValueError("Invalid expression")

if __name__ == '__main__':
    sample_expression = {
        "and": {
            "left": True,
            "right": False
        }
    }

    result = evaluate_nested_logic(sample_expression)
    print(result)