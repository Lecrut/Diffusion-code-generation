def validate_variables(variables):
    if not isinstance(variables, list) or len(variables) != 4:
        raise ValueError("Input must be a list of exactly four tuples.")
    expected_keys = ['A', 'B', 'C', 'D']
    for var in variables:
        if not isinstance(var, tuple) or len(var) != 2 or not all(isinstance(x, bool) for x in var):
            raise ValueError("Each variable must be a tuple of two boolean values.")
        if var[0] not in expected_keys:
            raise KeyError(f"Variable name must be one of {expected_keys}.")

def evaluate_expression(variables):
    validate_variables(variables)
    A, B = variables[0]
    C, D = variables[2]
    return (A and B) or (C and not D)

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression(sample_values)
    print(result)