VARS = ['A', 'B', 'C', 'D']

def evaluate_expression(variables):
    A, B, C, D = (variables[var] for var in VARS)
    return A and B or (C and (not D))
if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression({var: val for var, val in sample_values})
    print(result)