import re

def evaluate_boolean_expression(expression):
    pattern = '^\\s*(true|false)\\s*([&|\\^]\\s*(true|false)\\s*)*$'
    if not re.match(pattern, expression, re.IGNORECASE):
        raise ValueError('Invalid boolean expression')
    precedence = {'^': 2, '&': 1, '|': 0}

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '^':
            values.append(left != right)
        elif operator == '&':
            values.append(left and right)
        elif operator == '|':
            values.append(left or right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        elif expression[i] in '^&|':
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
        else:
            if expression[i].lower() == 'true':
                values.append(True)
            elif expression[i].lower() == 'false':
                values.append(False)
            i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    print(evaluate_boolean_expression('true & false'))
    print(evaluate_boolean_expression('(true | false) ^ true'))