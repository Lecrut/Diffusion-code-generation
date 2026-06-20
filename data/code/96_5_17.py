def evaluate_expression(variables):
    if not isinstance(variables, list) or len(variables) != 4:
        raise ValueError("Input must be a list of exactly four tuples.")
    for var, value in variables:
        if not isinstance(var, str) or not isinstance(value, bool):
            raise ValueError("Each tuple must contain a string and a boolean value.")
    
    A, B = variables[0][1], variables[1][1]
    C, D = variables[2][1], variables[3][1]
    return (A and B) or (C and not D)

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression(sample_values)
    print(result)