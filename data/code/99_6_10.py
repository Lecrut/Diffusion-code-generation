import re

def evaluate_boolean_expression(expression):
    pattern = '^\\s*(true|false)\\s*(and|or)?\\s*(true|false)\\s*$'
    if not re.match(pattern, expression, re.IGNORECASE):
        raise ValueError('Invalid boolean expression format')
    parts = expression.split()
    operand1 = parts[0].lower() == 'true'
    operator = parts[1] if len(parts) > 2 else None
    operand2 = parts[2].lower() == 'true' if operator else None
    if operator is None:
        return operand1
    elif operator.lower() == 'and':
        return operand1 and operand2
    elif operator.lower() == 'or':
        return operand1 or operand2
if __name__ == '__main__':
    try:
        result = evaluate_boolean_expression('true and false')
        print(result)
    except ValueError as e:
        print(e)