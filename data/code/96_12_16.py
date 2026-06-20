def evaluate_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] == '(':
            stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                apply_operator(operators, values)
            stack.pop()
            i += 1
        else:
            while stack and stack[-1] != '(' and greater_precedence(stack[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
    while operators:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    print(evaluate_expression('3 + 5 * (2 - 8)'))