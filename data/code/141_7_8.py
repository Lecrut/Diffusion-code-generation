def evaluate_expression(expression):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'AND':
            values.append(left and right)
        elif operator == 'OR':
            values.append(left or right)

    def greater_precedence(op1, op2):
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        return precedence[op1] > precedence[op2]

    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isalpha():
            j = i + 1
            while j < len(expression) and expression[j].isalpha():
                j += 1
            values.append(expression[i:j])
            i = j
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
        else:
            while (operators and operators[-1] != '(' and
                   greater_precedence(operators[-1], expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]

if __name__ == '__main__':
    print(evaluate_expression('NOT A AND B OR C'))