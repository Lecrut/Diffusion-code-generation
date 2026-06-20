def evaluate_nested_boolean(expression: str) -> bool:

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'AND':
            values.append(left and right)
        elif operator == 'OR':
            values.append(left or right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    if not expression:
        raise ValueError('Empty expression')
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
        elif expression[i:i + 3] in ('AND', 'OR'):
            operator = expression[i:i + 3]
            i += 3
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], operator):
                apply_operator(operators, values)
            operators.append(operator)
        elif expression[i:i + 4] == 'NOT':
            operator = expression[i:i + 4]
            i += 4
            if not (operators and operators[-1] == '('):
                while operators and greater_precedence('NOT', operators[-1]):
                    apply_operator(operators, values)
            operators.append(operator)
        else:
            value = int(expression[i])
            values.append(value)
            i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    sample_expression = 'NOT (3 AND 2 OR 1)'
    result = evaluate_nested_boolean(sample_expression)
    print(result)