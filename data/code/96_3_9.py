def evaluate_boolean_expression(expression):
    if not isinstance(expression, list) or len(expression) != 3:
        raise ValueError("Invalid boolean expression format")
    
    left = evaluate_boolean_expression(expression[0]) if isinstance(expression[0], list) else expression[0]
    operator = expression[1]
    right = evaluate_boolean_expression(expression[2]) if isinstance(expression[2], list) else expression[2]
    
    if operator == 'and':
        return left and right
    elif operator == 'or':
        return left or right
    else:
        raise ValueError("Unsupported operator")

if __name__ == '__main__':
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = evaluate_boolean_expression(sample_expression)
    print(result)