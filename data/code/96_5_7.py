VARIABLE_NAMES = ('A', 'B', 'C', 'D')

def evaluate_expression(variables):
    A, B = [variables[var] for var in VARIABLE_NAMES[:2]]
    C, D = [variables[var] for var in VARIABLE_NAMES[2:]]
    return A and B or (C and (not D))
if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression({var: value for var, value in sample_values})
    print(result)