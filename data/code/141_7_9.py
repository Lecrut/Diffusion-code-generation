def evaluate_expression(expression):

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'AND':
            values.append(left and right)
        elif operator == 'OR':
            values.append(left or right)
        elif operator == 'NOT':
            values.append(not right)

    def greater_precedence(op1, op2):
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        return precedence[op1] > precedence[op2]
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] in '()':
            if expression[i] == '(':
                operators.append(expression[i])
            else:
                while operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
            i += 1
        else:
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    sample_expression = '5 AND (3 OR NOT 2)'
    result = evaluate_expression(sample_expression)
    print(result)