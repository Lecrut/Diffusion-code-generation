def evaluate_formula(formula, inputs):
    return eval(formula, {'__builtins__': None}, inputs)

def formulas_equivalent(formula1, formula2, tolerance=1e-9, inputs=[0.5, -0.5, 0]):
    results1 = [evaluate_formula(formula1, {'x': x}) for x in inputs]
    results2 = [evaluate_formula(formula2, {'x': x}) for x in inputs]
    return all(abs(r1 - r2) <= tolerance for r1, r2 in zip(results1, results2))

if __name__ == '__main__':
    formula1 = 'x**2 + 3*x + 2'
    formula2 = '(x+1)*(x+2)'
    print(formulas_equivalent(formula1, formula2))