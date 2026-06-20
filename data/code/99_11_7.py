def evaluate_boolean_expression(expression):
    precedence = {'and': 1, 'or': 2, 'not': 3}
    tokens = expression.split()
    
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'and':
            values.append(left and right)
        elif operator == 'or':
            values.append(left or right)
    
    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    
    operators = []
    values = []
    
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            values.append(int(token))
        elif token == 'not':
            values.append(not values.pop())
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   greater_precedence(operators[-1], token)):
                apply_operator(operators, values)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False or not True"))
    print(not (False or True) and True)
    print(True and not (False and True))
    print((True or False) and (not False))