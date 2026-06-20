def evaluate_complex_logic(variables, conditions):
    for var_name, operator, value in conditions:
        if operator == '==':
            if variables[var_name] != value:
                return False
        elif operator == '<':
            if not (variables[var_name] < value):
                return False
        elif operator == '>':
            if not (variables[var_name] > value):
                return False
        elif operator == '<=':
            if not (variables[var_name] <= value):
                return False
        elif operator == '>=':
            if not (variables[var_name] >= value):
                return False
    return True

if __name__ == '__main__':
    sample_variables = {
        'age': 25,
        'access_level': "premium",
        'subscription_status': True
    }
    sample_conditions = [
        ('age', '>=', 18),
        ('access_level', '==', "premium"),
        ('subscription_status', '==', True)
    ]
    result = evaluate_complex_logic(sample_variables, sample_conditions)
    print("Access granted:", result)