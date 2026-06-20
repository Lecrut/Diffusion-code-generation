def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, inputs)

def compare_formulas(formula1, formula2, inputs, tolerance=1e-9):
    results1 = [evaluate_formula(formula1, {**inputs, 'x': x}) for x in inputs['x']]
    results2 = [evaluate_formula(formula2, {**inputs, 'x': x}) for x in inputs['x']]
    return all(abs(a - b) < tolerance for a, b in zip(results1, results2))

if __name__ == '__main__':
    formula1 = "x**2 + 3*x + 2"
    formula2 = "(x+1)*(x+2)"
    inputs = {'x': [-2, -1, 0, 1, 2]}
    print(compare_formulas(formula1, formula2, inputs))