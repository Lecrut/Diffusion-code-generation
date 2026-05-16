def evaluate_complex_logic(variables, conditions):
    for var_name, operator, required_value in conditions:
        if var_name not in variables:
            return False
        current_value = variables[var_name]
        result = False
        if operator == '==':
            result = (current_value == required_value)
        elif operator == '!=':
            result = (current_value != required_value)
        elif operator == '>':
            result = (current_value > required_value)
        elif operator == '<':
            result = (current_value < required_value)
        elif operator == '>=':
            result = (current_value >= required_value)
        elif operator == '<=':
            result = (current_value <= required_value)
        elif operator == 'and':
            result = True                                                            
        elif operator == 'or':
            result = True                                                            
        else:
            result = False
        if not result:
            return False
    return True
if __name__ == '__main__':
    sample_variables = {
        'A': 10,
        'B': 25,
        'C': 5,
        'D': 100
    }
    sample_conditions_true = [
        ('A', '==', 10),
        ('B', '>', 20),
        ('C', '<', 10),
        ('D', '>=', 90)
    ]
    sample_conditions_false = [
        ('A', '==', 11),
        ('B', '<', 25)
    ]
    print("--- Testing True Conditions ---")
    result_true = evaluate_complex_logic(sample_variables, sample_conditions_true)
    print(f"Variables: {sample_variables}")
    print(f"Conditions: {sample_conditions_true}")
    print(f"Result: {result_true}")
    print("\n--- Testing False Conditions ---")
    result_false = evaluate_complex_logic(sample_variables, sample_conditions_false)
    print(f"Variables: {sample_variables}")
    print(f"Conditions: {sample_conditions_false}")
    print(f"Result: {result_false}")
    sample_variables_incomplete = {
        'A': 10,
        'B': 25
    }
    print("\n--- Testing Incomplete Variables ---")
    result_incomplete = evaluate_complex_logic(sample_variables_incomplete, sample_conditions_true)
    print(f"Variables: {sample_variables_incomplete}")
    print(f"Conditions: {sample_conditions_true}")
    print(f"Result: {result_incomplete}")