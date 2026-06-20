def evaluate_formula(formula, inputs):
    return eval(formula, {"__builtins__": None}, inputs)

def compare_formulas(formula1, formula2, inputs, tolerance=1e-9):
    if not isinstance(formula1, str) or not isinstance(formula2, str):
        raise ValueError("Both formulas must be strings.")
    
    for key in inputs:
        if not isinstance(inputs[key], (list, tuple)) or not all(isinstance(x, (int, float)) for x in inputs[key]):
            raise ValueError(f"Inputs for {key} must be a list of numbers.")

    results1 = evaluate_formula(formula1, inputs)
    results2 = evaluate_formula(formula2, inputs)
    
    if isinstance(results1, dict) and isinstance(results2, dict):
        return all(abs(a - b) < tolerance for a, b in zip(results1.values(), results2.values()))
    elif isinstance(results1, list) and isinstance(results2, list):
        return all(all(abs(a - b) < tolerance for a, b in zip(sublist1, sublist2)) for sublist1, sublist2 in zip(results1, results2))
    else:
        raise ValueError("Results must be either both dictionaries or both lists of numbers.")

if __name__ == '__main__':
    formula1 = "x**2 + y**2"
    formula2 = "(x+y)**2 / 2"
    inputs = {'x': [0, 1, 2], 'y': [0, 1, 2]}
    print(compare_formulas(formula1, formula2, inputs))