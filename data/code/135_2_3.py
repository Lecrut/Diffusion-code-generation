import math

def evaluate_formula(formula, inputs):
    return eval(formula, {'__builtins__': None}, inputs)

def are_formulas_equivalent(formula1, formula2, tolerance=1e-9):
    test_inputs = [0.5, 1.0, -1.0, math.pi, math.e]
    results1 = {x: evaluate_formula(formula1, {'x': x}) for x in test_inputs}
    results2 = {x: evaluate_formula(formula2, {'x': x}) for x in test_inputs}

    return all(abs(results1[x] - results2[x]) < tolerance for x in test_inputs)

if __name__ == '__main__':
    formula1 = 'x**2 + 2*x + 1'
    formula2 = '(x+1)**2'
    print(are_formulas_equivalent(formula1, formula2))