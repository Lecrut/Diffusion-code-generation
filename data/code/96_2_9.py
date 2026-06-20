def evaluate_expression(expression: str, variables: dict) -> bool:
    def parse_and_evaluate(tokens):
        if len(tokens) == 1:
            return variables[tokens[0]]
        
        op = tokens[1]
        left = parse_and_evaluate(tokens[:2])
        right = parse_and_evaluate(tokens[2:])
        
        if op == 'and':
            return left and right
        elif op == 'or':
            return left or right
    
    def tokenize(expression):
        expression = expression.replace('(', ' ( ')
        expression = expression.replace(')', ' ) ')
        tokens = expression.split()
        return tokens
    
    tokens = tokenize(expression)
    return parse_and_evaluate(tokens)

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    result = evaluate_expression(expr, vars_dict)
    print(result)