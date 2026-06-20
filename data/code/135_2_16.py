import math

def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, {"x": x})

def formulas_equivalent(formula1, formula2, tolerance=1e-9, inputs=[0, 1, -1, math.pi, -math.pi]):
    results1 = {x: evaluate_formula(formula1, x) for x in inputs}
    results2 = {x: evaluate_formula(formula2, x) for x in inputs}
    
    return all(math.isclose(v1, v2, rel_tol=tolerance) for v1, v2 in zip(results1.values(), results2.values()))

if __name__ == '__main__':
    formula1 = "x**2 + 2*x + 1"
    formula2 = "(x+1)**2"
    
    print(formulas_equivalent(formula1, formula2))