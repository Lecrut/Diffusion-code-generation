def evaluate_complex_logic(variables, conditions):
    for var_name, operator, required_value in conditions:
        if var_name not in variables:
            return False
        var_value = variables[var_name]
        result = False
        if operator == '==':
            result = (var_value == required_value)
        elif operator == '!=':
            result = (var_value != required_value)
        elif operator == '>':
            result = (var_value > required_value)
        elif operator == '<':
            result = (var_value < required_value)
        elif operator == '>=':
            result = (var_value >= required_value)
        elif operator == '<=':
            result = (var_value <= required_value)
        elif operator == 'and':
            continue
        elif operator == 'or':
            continue
        else:
            continue
        if not result:
            return False
    return True
if __name__ == '__main__':
    sample_variables = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 15
    }
    sample_conditions_true = [
        ('A', '>=', 10),
        ('B', '!=', 10),
        ('C', '<', 10)
    ]
    sample_conditions_false = [
        ('A', '>', 50),
        ('B', '==', 10)
    ]
    print("Testing with True conditions:")
    result1 = evaluate_complex_logic(sample_variables, sample_conditions_true)
    print(f"Result 1: {result1}")
    print("\nTesting with False conditions:")
    result2 = evaluate_complex_logic(sample_variables, sample_conditions_false)
    print(f"Result 2: {result2}")
    sample_variables_empty = {}
    sample_conditions_with_missing = [
        ('A', '==', 10)
    ]
    print("\nTesting with missing variable:")
    result3 = evaluate_complex_logic(sample_variables_empty, sample_conditions_with_missing)
    print(f"Result 3: {result3}")