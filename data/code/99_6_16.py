import re

def evaluate_boolean_expression(expression):
    pattern = '^\\s*(true|false)\\s*|\\s*(\\w+)\\s*(and|or)\\s*(\\w+)\\s*$'
    if not re.match(pattern, expression, re.IGNORECASE):
        raise ValueError('Invalid boolean expression structure')
    parts = expression.split()
    if len(parts) == 3:
        left, operator, right = parts
        if operator.lower() == 'and':
            return evaluate_boolean_expression(left) and evaluate_boolean_expression(right)
        elif operator.lower() == 'or':
            return evaluate_boolean_expression(left) or evaluate_boolean_expression(right)
    return expression.lower() == 'true'
if __name__ == '__main__':
    print(evaluate_boolean_expression('true'))
    print(evaluate_boolean_expression('false'))
    print(evaluate_boolean_expression('a and b'))
    print(evaluate_boolean_expression('c or d'))
    print(evaluate_boolean_expression('(e and f) or g'))