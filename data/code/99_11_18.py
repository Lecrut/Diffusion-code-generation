def evaluate_boolean_expression(expression):
    operators = {
        'and': lambda x, y: x and y,
        'or': lambda x, y: x or y,
        'not': lambda x: not x
    }
    
    precedence = {'not': 3, 'and': 2, 'or': 1}
    
    def apply_operator(op, stack):
        right = stack.pop()
        left = stack.pop()
        result = operators[op](left, right)
        stack.append(result)
    
    def evaluate(tokens):
        stack = []
        operator_stack = []
        
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            elif token == 'not':
                apply_operator('not', stack)
            elif token in operators:
                while (operator_stack and 
                       precedence[token] <= precedence.get(operator_stack[-1], 0)):
                    apply_operator(operator_stack.pop(), stack)
                operator_stack.append(token)
        
        while operator_stack:
            apply_operator(operator_stack.pop(), stack)
        
        return stack[0]
    
    tokens = expression.split()
    result = evaluate(tokens)
    print(result)

if __name__ == '__main__':
    print(evaluate_boolean_expression('True and False or (not True)'))
    print(not (False or True) and True)
    print(True and not (False and True))
    print((True or False) and (not False))