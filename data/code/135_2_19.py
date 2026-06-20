import math

def evaluate_formula(formula, inputs):
    return eval(formula, {'math': math}, {**inputs})

def verify_equivalence(formula1, formula2, inputs, tolerance=1e-9):
    results1 = [evaluate_formula(formula1, {f'x{i}': x}) for i, x in enumerate(inputs)]
    results2 = [evaluate_formula(formula2, {f'x{i}': x}) for i, x in enumerate(inputs)]
    return all(abs(r1 - r2) < tolerance for r1, r2 in zip(results1, results2))

if __name__ == '__main__':
    formula1 = 'math.sin(x0) + math.cos(x1)'
    formula2 = 'math.cos(x1) + math.sin(x0)'
    inputs = [0.5, 1.0]
    print(verify_equivalence(formula1, formula2, inputs))