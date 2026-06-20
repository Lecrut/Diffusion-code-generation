def evaluate_expression(expr):
    stack = []
    operators = set(['AND', 'OR', 'NOT'])
    
    def apply_operator(op, b, a=None):
        if op == 'AND':
            return a and b
        elif op == 'OR':
            return a or b
        elif op == 'NOT':
            return not b
    
    for token in expr.split():
        if token in operators:
            stack.append(token)
        else:
            try:
                value = int(token)
                while stack and stack[-1] != 'NOT':
                    operator = stack.pop()
                    right = stack.pop()
                    left = None if len(stack) == 0 else stack.pop()
                    result = apply_operator(operator, right, left)
                    stack.append(result)
                stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    while len(stack) > 1:
        operator = stack.pop()
        right = stack.pop()
        left = None if len(stack) == 0 else stack.pop()
        result = apply_operator(operator, right, left)
        stack.append(result)
    
    return stack[0]

if __name__ == '__main__':
    expr = "5 AND 3 OR NOT 7"
    try:
        result = evaluate_expression(expr)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)