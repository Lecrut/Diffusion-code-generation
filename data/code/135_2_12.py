def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, inputs)

def are_formulas_equivalent(formula1, formula2, inputs, tolerance=1e-9):
    result1 = evaluate_formula(formula1, inputs)
    result2 = evaluate_formula(formula2, inputs)
    return abs(result1 - result2) <= tolerance

if __name__ == '__main__':
    formula1 = "x**2 + 2*x + 1"
    formula2 = "(x+1)**2"
    inputs = {"x": 3}
    print(are_formulas_equivalent(formula1, formula2, inputs))