def evaluate_logical_expression(expression):
    stack = []
    operators = set(['and', 'or'])
    
    def apply_operator(op, a, b):
        if op == 'and':
            return a and b
        elif op == 'or':
            return a or b
    
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token) != 0)
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Syntax error: too few operands")
            right = stack.pop()
            left = stack.pop()
            result = apply_operator(token, left, right)
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Syntax error: too many operands")
    
    return stack[0]

if __name__ == '__main__':
    expression = "1 and (2 or 3)"
    result = evaluate_logical_expression(expression)
    print(result)