def validate_expression(expression):
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    if len(tokens) % 2 != 1:
        raise ValueError("Invalid number of operands and operators")
    for i in range(0, len(tokens), 2):
        if not tokens[i].isdigit():
            raise ValueError(f"Invalid operand: {tokens[i]}")

def evaluate_predicate(expression, values):
    validate_expression(expression)
    tokens = expression.split()
    value_map = {f'v{i}': val for i, val in enumerate(values)}
    
    def eval_term(token):
        if token.isdigit():
            return int(token)
        elif token.startswith('v'):
            return value_map[token]
        else:
            raise NameError(f"Undefined variable or constant: {token}")
    
    stack = []
    for token in tokens:
        if token.isdigit() or token.startswith('v'):
            stack.append(eval_term(token))
        elif token in ('and', 'or', 'not'):
            right = stack.pop()
            left = stack.pop()
            if token == 'and':
                result = left and right
            elif token == 'or':
                result = left or right
            else:
                result = not right
            stack.append(result)
    
    return stack[0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4]
    sample_expression = "v0 and v1 or v2 and not v3"
    print(evaluate_predicate(sample_expression, sample_values))