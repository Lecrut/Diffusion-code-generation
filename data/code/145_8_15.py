def evaluate_logical_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    values_map = {f'v{i}': val for i, val in enumerate(values)}
    
    def is_operator(token):
        return token in ('and', 'or')
    
    def evaluate_term(tokens_list):
        stack = []
        while tokens_list:
            token = tokens_list.pop(0)
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            elif is_operator(token):
                right = stack.pop()
                left = stack.pop()
                if token == 'and':
                    stack.append(left and right)
                elif token == 'or':
                    stack.append(left or right)
        return stack[0]
    
    def evaluate_expression(expression_list):
        tokens = expression_list.split()
        return evaluate_term(tokens)
    
    try:
        result = evaluate_expression(' '.join(tokens))
        return result
    except (ValueError, KeyError) as e:
        raise ValueError("Invalid expression or undefined variable") from e

if __name__ == '__main__':
    sample_values = [10, 20, 30]
    sample_expression = "v0 and v1 or v2"
    print(evaluate_logical_expression(sample_expression, sample_values))