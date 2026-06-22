def evaluate_complex_logic(variables, conditions):
    def check_condition(var_name, operator, target_value):
        if var_name not in variables:
            return False
        current_value = variables[var_name]
        if operator == '==':
            return current_value == target_value
        if operator == '!=':
            return current_value != target_value
        if operator == '>':
            return current_value > target_value
        if operator == '<':
            return current_value < target_value
        if operator == '>=':
            return current_value >= target_value
        if operator == '<=':
            return current_value <= target_value
        if operator == 'in':
            return current_value in target_value
        if operator == 'not in':
            return current_value not in target_value
        raise ValueError(f"Operator '{operator}' is not supported.")

    for condition in conditions:
        if not check_condition(*condition):
            return False
    return True

if __name__ == '__main__':
    sample_vars = {
        'age': 25,
        'score': 85,
        'status': 'active',
        'tags': ['admin', 'user']
    }
    sample_conds = [
        ('age', '>=', 18),
        ('score', '>', 80),
        ('status', '==', 'active'),
        ('tags', 'in', ['admin', 'user'])
    ]
    result = evaluate_complex_logic(sample_vars, sample_conds)
    print(result)