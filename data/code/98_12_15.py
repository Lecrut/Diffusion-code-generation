def evaluate_complex_logic(variables, conditions):
    if not isinstance(variables, dict) or not all((isinstance(k, str) and isinstance(v, (int, float)) for k, v in variables.items())):
        raise ValueError('Variables must be a dictionary with string keys and numeric values.')
    if not isinstance(conditions, list) or not all((isinstance(c, tuple) and len(c) == 3 for c in conditions)):
        raise ValueError('Conditions must be a list of tuples with exactly three elements each.')
    for var_name, operator, value in conditions:
        if var_name not in variables:
            raise KeyError(f"Variable '{var_name}' not found in provided variables.")
        if operator == '==':
            if variables[var_name] != value:
                return False
        elif operator == '<':
            if variables[var_name] >= value:
                return False
        elif operator == '>':
            if variables[var_name] <= value:
                return False
        elif operator == '<=':
            if variables[var_name] > value:
                return False
        elif operator == '>=':
            if variables[var_name] < value:
                return False
        else:
            raise ValueError(f'Unsupported operator: {operator}')
    return True
if __name__ == '__main__':
    sample_variables = {'age': 25, 'balance': 100.0, 'is_active': True}
    sample_conditions = [('age', '>=', 18), ('balance', '>', 50.0), ('is_active', '==', True)]
    result = evaluate_complex_logic(sample_variables, sample_conditions)
    print(result)