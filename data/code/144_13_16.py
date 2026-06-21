def evaluate_boolean_expression(expression):
    from itertools import product

    variables = set(expression) - {'A', 'B', 'C'}
    results = {}

    for A, B, C in product([True, False], repeat=3):
        env = {'A': A, 'B': B, 'C': C}
        result = eval(expression, {}, env)
        results[(A, B, C)] = result

    return results

if __name__ == '__main__':
    expression = "A and (not B or C)"
    print(evaluate_boolean_expression(expression))