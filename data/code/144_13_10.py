from itertools import product

def evaluate_boolean_expression(expression):
    variables = set(expression) - {' ', '(', ')', '&', '|'}
    results = {}
    for A, B, C in product([True, False], repeat=3):
        expr_vars = {var: val for var, val in zip(variables, (A, B, C))}
        result = eval(expression, expr_vars)
        results[(A, B, C)] = result
    return results

if __name__ == '__main__':
    expression = "A & (B | ~C)"
    print(evaluate_boolean_expression(expression))