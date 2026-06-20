import math

def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, inputs)

def are_formulas_equivalent(formula1, formula2, inputs, tolerance=1e-9):
    results1 = {input_val: evaluate_formula(formula1, {'x': input_val}) for input_val in inputs}
    results2 = {input_val: evaluate_formula(formula2, {'x': input_val}) for input_val in inputs}
    
    return all(abs(result1 - result2) <= tolerance for result1, result2 in zip(results1.values(), results2.values()))

if __name__ == '__main__':
    formula1 = 'math.sin(x)'
    formula2 = 'math.cos(math.pi/2 - x)'
    inputs = range(-10, 11)
    
    print(are_formulas_equivalent(formula1, formula2, inputs))