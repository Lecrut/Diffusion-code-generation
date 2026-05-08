def evaluate_complex_logic(variables, conditions):
    for var_name, operator, required_value in conditions:
        if var_name not in variables:
            return False
        actual_value = variables[var_name]
        condition_met = False
        if operator == '==':
            condition_met = (actual_value == required_value)
        elif operator == '!=':
            condition_met = (actual_value != required_value)
        elif operator == '>':
            condition_met = (actual_value > required_value)
        elif operator == '<':
            condition_met = (actual_value < required_value)
        elif operator == '>=':
            condition_met = (actual_value >= required_value)
        elif operator == '<=':
            condition_met = (actual_value <= required_value)
        elif operator == 'in':
            condition_met = (actual_value in [required_value])
        else:
            continue
        if not condition_met:
            return False
    return True
if __name__ == '__main__':
    sample_variables = {
        'age': 30,
        'score': 85,
        'is_active': True,
        'city': 'New York'
    }
    sample_conditions = [
        ('age', '>=', 18),
        ('score', '>', 80),
        ('is_active', '==', True),
        ('city', 'in', ['New York', 'Los Angeles'])
    ]
    result = evaluate_complex_logic(sample_variables, sample_conditions)
    print(result)
    sample_variables_fail = {
        'age': 15,
        'score': 90,
        'is_active': True,
        'city': 'Chicago'
    }
    result_fail = evaluate_complex_logic(sample_variables_fail, sample_conditions)
    print(result_fail)