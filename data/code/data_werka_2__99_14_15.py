def evaluate_expression(expression):
    tokens = expression.split()
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '(':
            stack.append(token)
        elif token == ')':
            sub_stack = []
            while stack and stack[-1] != '(':
                sub_stack.append(stack.pop())
            stack.pop()
            result = _evaluate_tokens(sub_stack)
            stack.append(result)
        elif token in ('AND', 'OR', 'NOT'):
            stack.append(token)
        else:
            val = token.lower() == 'true'
            stack.append(val)
        i += 1
    return _evaluate_tokens(stack)

def _evaluate_tokens(tokens):
    if not tokens:
        return False
    if len(tokens) == 1:
        return tokens[0]
    
    and_stack = []
    for token in tokens:
        if token == 'AND':
            if len(and_stack) < 2:
                raise ValueError("Invalid expression")
            b = and_stack.pop()
            a = and_stack.pop()
            and_stack.append(a and b)
        else:
            and_stack.append(token)
    
    or_stack = []
    for token in and_stack:
        if token == 'OR':
            if len(or_stack) < 2:
                raise ValueError("Invalid expression")
            b = or_stack.pop()
            a = or_stack.pop()
            or_stack.append(a or b)
        else:
            or_stack.append(token)
    
    if len(or_stack) != 1:
        raise ValueError("Invalid expression")
    
    result = or_stack[0]
    if isinstance(result, bool):
        return result
    
    not_stack = []
    for token in or_stack:
        if token == 'NOT':
            if len(not_stack) < 1:
                raise ValueError("Invalid expression")
            val = not_stack.pop()
            not_stack.append(not val)
        else:
            not_stack.append(token)
    
    if len(not_stack) != 1:
        raise ValueError("Invalid expression")
    
    return not_stack[0]

if __name__ == '__main__':
    expr1 = "True AND False OR True"
    result1 = evaluate_expression(expr1)
    print(result1)
    
    expr2 = "NOT True AND False"
    result2 = evaluate_expression(expr2)
    print(result2)
    
    expr3 = "(True OR False) AND NOT False"
    result3 = evaluate_expression(expr3)
    print(result3)