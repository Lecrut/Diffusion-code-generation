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
        'balance': 1500.50
    }
    sample_conditions = [
        ('age', '>=', 18),
        ('score', '>', 80),
        ('is_active', '==', True),
        ('balance', '<=', 2000.00)
    ]
    result = evaluate_complex_logic(sample_variables, sample_conditions)
    print(result)
    sample_variables_fail = {
        'age': 15,
        'score': 90,
        'is_active': True,
        'balance': 1000.00
    }
    sample_conditions_fail = [
        ('age', '>=', 18),
        ('score', '>', 80)
    ]
    result_fail = evaluate_complex_logic(sample_variables_fail, sample_conditions_fail)
    print(result_fail)