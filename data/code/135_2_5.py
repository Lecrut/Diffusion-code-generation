import math

def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, inputs)

def are_formulas_equivalent(formula1, formula2, tolerance=1e-9):
    test_inputs = [0.5, 1.0, -1.0, math.pi, math.e]
    for input_val in test_inputs:
        result1 = evaluate_formula(formula1, {"x": input_val})
        result2 = evaluate_formula(formula2, {"x": input_val})
        if not math.isclose(result1, result2, rel_tol=tolerance):
            return False
    return True

if __name__ == '__main__':
    formula1 = "x**2 + 3*x + 2"
    formula2 = "(x+1)*(x+2)"
    print(are_formulas_equivalent(formula1, formula2))