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
            result = False 
        else:
            result = False
        if not result:
            return False
    return True
if __name__ == '__main__':
    sample_variables = {
        'A': 10,
        'B': 25,
        'C': 50,
        'D': 100
    }
    sample_conditions = [
        ('A', '==', 10),
        ('B', '>', 20),
        ('C', '<=', 60),
        ('D', '!=', 100)
    ]
    result1 = evaluate_complex_logic(sample_variables, sample_conditions)
    print(f"Result 1: {result1}")
    sample_variables_2 = {
        'A': 10,
        'B': 15,
        'C': 50
    }
    sample_conditions_2 = [
        ('A', '==', 10),
        ('B', '>', 20),
        ('C', '<=', 40)
    ]
    result2 = evaluate_complex_logic(sample_variables_2, sample_conditions_2)
    print(f"Result 2: {result2}")
    sample_variables_3 = {
        'A': 10,
        'B': 25,
        'C': 50,
        'D': 100
    }
    sample_conditions_3 = [
        ('A', '==', 10),
        ('B', '>', 20),
        ('D', '==', 100)
    ]
    result3 = evaluate_complex_logic(sample_variables_3, sample_conditions_3)
    print(f"Result 3: {result3}")