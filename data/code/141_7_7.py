def evaluate_expression(expression):

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'AND':
            values.append(left and right)
        elif operator == 'OR':
            values.append(left or right)
    precedence = {'AND': 2, 'OR': 1}
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
        elif expression[i] in 'ANDOR':
            while operators and operators[-1] != '(' and (precedence[operators[-1]] >= precedence[expression[i]]):
                apply_operator(operators, values)
            operators.append(expression[i])
        else:
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j - 1
        i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    sample_expression = '3 AND (2 OR 4)'
    print(evaluate_expression(sample_expression))