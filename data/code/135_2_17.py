import math
TOLERANCE = 1e-09
TEST_INPUTS = {'x': [0, 1, 2], 'y': [0, 1, 2]}

def evaluate_formula(formula, inputs):
    return eval(formula, {'__builtins__': None}, inputs)

def compare_formulas(formula1, formula2, inputs=TEST_INPUTS, tolerance=TOLERANCE):
    results1 = {x: evaluate_formula(formula1, {'x': x, 'y': y}) for x in inputs['x'] for y in inputs['y']}
    results2 = {x: evaluate_formula(formula2, {'x': x, 'y': y}) for x in inputs['x'] for y in inputs['y']}
    return all((abs(a - b) < tolerance for a, b in zip(results1.values(), results2.values())))
if __name__ == '__main__':
    formula1 = 'x**2 + y**2'
    formula2 = '(x+y)**2 / 2'
    print(compare_formulas(formula1, formula2))