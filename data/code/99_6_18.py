import re

def evaluate_boolean_expression(expression):
    precedence = {'and': 2, 'or': 1}
    tokens = re.findall('\\b\\w+\\b|\\(|\\)', expression)

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'and':
            values.append(left and right)
        elif operator == 'or':
            values.append(left or right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    operators = []
    values = []
    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], token):
                apply_operator(operators, values)
            operators.append(token)
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    expression = '3 and 5 or 2'
    result = evaluate_boolean_expression(expression)
    print(result)