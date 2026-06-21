from itertools import product

def evaluate_expression(expression):
    results = {}
    for A, B, C in product([True, False], repeat=3):
        result = eval(expression, {'A': A, 'B': B, 'C': C})
        results[(A, B, C)] = result
    return results

if __name__ == '__main__':
    expression = "A and (not B or C)"
    print(evaluate_expression(expression))