def evaluate_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                right = stack.pop()
                left = stack.pop()
                operator = stack.pop()
                result = apply_operator(left, right, operator)
                stack.append(result)
            stack.pop()
        elif char in operators:
            while stack and stack[-1] != '(' and (precedence(char) <= precedence(stack[-1])):
                right = stack.pop()
                left = stack.pop()
                operator = stack.pop()
                result = apply_operator(left, right, operator)
                stack.append(result)
            stack.append(char)
    while len(stack) > 1:
        right = stack.pop()
        left = stack.pop()
        operator = stack.pop()
        result = apply_operator(left, right, operator)
        stack.append(result)
    return stack[0]

def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    else:
        return 0

def apply_operator(left, right, operator):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        return left / right
if __name__ == '__main__':
    expression = '3+5*(2-8)'
    result = evaluate_expression(expression)
    print(result)