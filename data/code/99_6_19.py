import re

def evaluate_boolean_expression(expression):
    pattern = '^\\s*(true|false)\\s*([&|\\^]\\s*(true|false)\\s*)*$'
    if not re.match(pattern, expression, re.IGNORECASE):
        raise ValueError('Invalid boolean expression')
    precedence = {'&': 2, '|': 1, '^': 0}
    stack_values = []
    stack_operators = []
    tokens = re.findall('\\b(true|false)\\b|[&|\\^]', expression, re.IGNORECASE)
    for token in tokens:
        if token.lower() == 'true' or token.lower() == 'false':
            stack_values.append(True if token.lower() == 'true' else False)
        else:
            while stack_operators and precedence[stack_operators[-1]] >= precedence[token]:
                operator = stack_operators.pop()
                right = stack_values.pop()
                left = stack_values.pop()
                if operator == '&':
                    stack_values.append(left and right)
                elif operator == '|':
                    stack_values.append(left or right)
                else:
                    stack_values.append(not left ^ right)
            stack_operators.append(token)
    while stack_operators:
        operator = stack_operators.pop()
        right = stack_values.pop()
        left = stack_values.pop()
        if operator == '&':
            stack_values.append(left and right)
        elif operator == '|':
            stack_values.append(left or right)
        else:
            stack_values.append(not left ^ right)
    return stack_values[0]
if __name__ == '__main__':
    expression = 'true & false | true'
    result = evaluate_boolean_expression(expression)
    print(result)