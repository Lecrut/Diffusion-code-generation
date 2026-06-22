def evaluate_complex_logic(variables, conditions):
    operators = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
    }
    for var_name, op, val in conditions:
        if var_name not in variables:
            return False
        actual_value = variables[var_name]
        if op not in operators:
            raise ValueError(f"Unsupported operator: {op}")
        if not operators[op](actual_value, val):
            return False
    return True

if __name__ == '__main__':
    vars_dict = {'x': 10, 'y': 20, 'z': 'hello'}
    required_conditions = [
        ('x', '>', 5),
        ('y', '==', 20),
        ('z', '==', 'hello')
    ]
    result = evaluate_complex_logic(vars_dict, required_conditions)
    print(result)