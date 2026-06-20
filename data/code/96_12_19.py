def evaluate_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

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
        elif operator == '^':
            values.append(left ** right)
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] in operators:
            while stack and stack[-1] != '(' and (precedence[stack[-1]] >= precedence[expression[i]]):
                apply_operator(operators, values)
            stack.append(expression[i])
            i += 1
        elif expression[i] == '(':
            stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                apply_operator(operators, values)
            stack.pop()
            i += 1
    while stack:
        apply_operator(operators, values)
    return values[0]
if __name__ == '__main__':
    expression = '3 + 5 * (2 - 8)'
    result = evaluate_expression(expression)
    print(result)