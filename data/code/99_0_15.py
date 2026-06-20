import operator

def evaluate_expression(expression):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow, '%': operator.mod, '//': operator.floordiv}

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(ops[operator](left, right))

    def greater_precedence(op1, op2):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3, '%': 2, '//': 2}
        return precedence[op1] > precedence[op2]
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        elif expression[i].isdigit() or expression[i] == '.':
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            values.append(float(expression[i:j]))
            i = j
        elif expression[i] in ops:
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    print(evaluate_expression('3 + 5 * (2 - 8)'))