def validate_variables(variables):
    expected_keys = {'A', 'B', 'C', 'D'}
    if not isinstance(variables, dict) or not all(k in variables and isinstance(v, bool) for k, v in variables.items()):
        raise ValueError("Input must be a dictionary with keys A, B, C, D and boolean values.")
    if expected_keys != set(variables.keys()):
        raise KeyError(f"Dictionary must contain exactly the keys {expected_keys}.")

def evaluate_expression(variables):
    validate_variables(variables)
    return (variables['A'] and variables['B']) or (variables['C'] and not variables['D'])

if __name__ == '__main__':
    sample_values = {'A': True, 'B': False, 'C': True, 'D': False}
    result = evaluate_expression(sample_values)
    print(result)