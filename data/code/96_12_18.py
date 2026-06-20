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
        elif expression[i] == '(':
            stack.append(expression[i])
        elif expression[i] in operators:
            while stack and stack[-1] != '(' and greater_precedence(stack[-1], expression[i]):
                apply_operator(stack, values)
            stack.append(expression[i])
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                apply_operator(stack, values)
            stack.pop()
        else:
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j - 1
        i += 1
    while stack:
        apply_operator(stack, values)
    return values[0]
if __name__ == '__main__':
    print(evaluate_expression('3 + 5 * (2 - 8)'))