def evaluate_expression(variables):
    env = dict(variables)
    a = env.get('A', False)
    b = env.get('B', False)
    c = env.get('C', False)
    d = env.get('D', False)
    return (a and b) or (c and (not d))

if __name__ == '__main__':
    inputs = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression(inputs)
    print(result)