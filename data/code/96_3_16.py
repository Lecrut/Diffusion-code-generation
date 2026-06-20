def evaluate_expression(expression):
    if isinstance(expression, list) and len(expression) == 3:
        left = evaluate_expression(expression[0])
        operator = expression[1]
        right = evaluate_expression(expression[2])
        return eval(f"{left} {operator} {right}")
    else:
        return expression

if __name__ == '__main__':
    sample_expression = [['A', 'and', 'B'], 'or', ['C', 'and', 'D']]
    result = evaluate_expression(sample_expression)
    print(result)