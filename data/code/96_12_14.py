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
            stack.append(int(token) != 0)
        elif token in operators:
            apply_operator(token)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Expression is not fully evaluated")
    
    return stack[0]

if __name__ == '__main__':
    try:
        result = evaluate_expression("(1 and 0 or 1)")
        print(result)
    except Exception as e:
        print(e)