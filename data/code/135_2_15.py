import numpy as np

def evaluate_formula(formula, inputs):
    return eval(formula, {'__builtins__': None}, inputs)

def are_formulas_equivalent(formula1, formula2, tolerance=1e-6):
    test_inputs = {
        'x': np.linspace(-10, 10, 100),
        'y': np.linspace(-5, 5, 100)
    }
    
    results1 = evaluate_formula(formula1, test_inputs)
    results2 = evaluate_formula(formula2, test_inputs)
    
    return np.allclose(results1, results2, atol=tolerance)

if __name__ == '__main__':
    formula1 = 'x**2 + y**2'
    formula2 = '(x*x) + (y*y)'
    
    print(are_formulas_equivalent(formula1, formula2))