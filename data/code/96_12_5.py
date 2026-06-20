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
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            apply_operator(token)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[0]

if __name__ == '__main__':
    print(evaluate_expression("1 and 0 or 1"))