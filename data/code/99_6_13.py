import re

def evaluate_boolean_expression(expression):
    pattern = '^\\s*(?:true|false)\\s*([&|\\^])\\s*(?:true|false)\\s*$'
    if not re.match(pattern, expression, re.IGNORECASE):
        raise ValueError('Invalid boolean expression format')
    parts = expression.split()
    operator = parts[1].lower()
    left_value = parts[0].lower() == 'true'
    right_value = parts[2].lower() == 'true'
    if operator == '&':
        return left_value and right_value
    elif operator == '|':
        return left_value or right_value
    elif operator == '^':
        return left_value != right_value
if __name__ == '__main__':
    try:
        result = evaluate_boolean_expression('true & false')
        print(result)
    except ValueError as e:
        print(e)