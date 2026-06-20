def evaluate_boolean_expression(expression):
    if isinstance(expression, list) and len(expression) == 3:
        left = evaluate_boolean_expression(expression[0])
        operator = expression[1]
        right = evaluate_boolean_expression(expression[2])
        if operator == 'and':
            return left and right
        elif operator == 'or':
            return left or right
    else:
        return bool(expression)

if __name__ == '__main__':
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = evaluate_boolean_expression(sample_expression)
    print(result)