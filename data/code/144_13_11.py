def evaluate_boolean_expression(expression):
    from itertools import product

    variables = set(expression) - {'A', 'B', 'C'}
    if not variables:
        raise ValueError("Expression must contain at least one variable.")

    results = {}
    for A, B, C in product([True, False], repeat=3):
        result = eval(expression.replace('A', str(A)).replace('B', str(B)).replace('C', str(C)))
        results[(A, B, C)] = result

    return results

if __name__ == '__main__':
    expression = "A and (not B or C)"
    print(evaluate_boolean_expression(expression))