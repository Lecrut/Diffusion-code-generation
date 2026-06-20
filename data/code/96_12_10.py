def evaluate_expression(expression):
    stack = []
    operators = set(['and', 'or'])
    
    def apply_operator(op):
        right = stack.pop()
        left = stack.pop()
        if op == 'and':
            stack.append(left and right)
        elif op == 'or':
            stack.append(left or right)
    
    tokens = expression.split()
    for token in tokens:
        if token in operators:
            while stack and isinstance(stack[-1], bool):
                apply_operator(stack.pop())
            stack.append(token)
        else:
            try:
                value = eval(token, {'__builtins__': None}, {})
                stack.append(value)
            except (SyntaxError, NameError):
                return False
    
    while len(stack) > 1:
        apply_operator(stack.pop())
    
    return stack[0]

if __name__ == '__main__':
    print(evaluate_expression("True and False or True"))