def evaluate_nested_boolean(expression):
    stack = []
    operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y}
    
    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
        else:
            stack.append(token == 'true')
    
    return stack[0]

if __name__ == '__main__':
    sample_expression = "NOT (true AND false) OR true"
    print(evaluate_nested_boolean(sample_expression))