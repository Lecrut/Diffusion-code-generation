def evaluate_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    
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
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            while (stack and stack[-1] != '(' and
                   operators.index(stack[-1]) >= operators.index(token)):
                apply_operator(operators, stack)
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                apply_operator(operators, stack)
            stack.pop()
    
    while stack and len(stack) > 1:
        apply_operator(operators, stack)
    
    return stack[0]

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))