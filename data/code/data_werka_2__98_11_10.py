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
        raise ValueError(f"Unsupported operator: {operator}")

    for var_name, operator, target_value in conditions:
        if not check_condition(var_name, operator, target_value):
            return False
    return True

if __name__ == '__main__':
    sample_vars = {'x': 10, 'y': 'hello', 'z': [1, 2, 3]}
    sample_conds = [
        ('x', '>', 5),
        ('y', '==', 'hello'),
        ('z', 'in', [1, 2, 3, 4])
    ]
    result = evaluate_complex_logic(sample_vars, sample_conds)
    print(result)