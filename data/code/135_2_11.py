import math

def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, {"x": inputs})

def are_formulas_equivalent(formula1, formula2, tolerance=1e-9, inputs=[0.5, 1.0, -1.0]):
    results1 = [evaluate_formula(formula1, x) for x in inputs]
    results2 = [evaluate_formula(formula2, x) for x in inputs]
    return all(math.isclose(r1, r2, rel_tol=tolerance) for r1, r2 in zip(results1, results2))

if __name__ == '__main__':
    formula1 = "x**2 + 2*x + 1"
    formula2 = "(x+1)**2"
    print(are_formulas_equivalent(formula1, formula2))