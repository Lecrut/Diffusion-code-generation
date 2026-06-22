def evaluate_expression(variables):
    env = dict(variables)
    A = env.get('A', False)
    B = env.get('B', False)
    C = env.get('C', False)
    D = env.get('D', False)
    return (A and B) or (C and (not D))

if __name__ == '__main__':
    inputs = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression(inputs)
    print(result)