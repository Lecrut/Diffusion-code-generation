def evaluate_complex_logic(variables, conditions):
    if not isinstance(variables, dict):
        raise ValueError("variables must be a dictionary")
    if not isinstance(conditions, list):
        raise ValueError("conditions must be a list")
    
    for condition in conditions:
        if not isinstance(condition, tuple) or len(condition) != 3:
            raise ValueError("Each condition must be a tuple of (variable_name, operator, value)")
        
        var_name, operator, expected_value = condition
        
        if var_name not in variables:
            return False
        
        actual_value = variables[var_name]
        
        if operator == '==':
            if not (actual_value == expected_value):
                return False
        elif operator == '!=':
            if not (actual_value != expected_value):
                return False
        elif operator == '>':
            if not (actual_value > expected_value):
                return False
        elif operator == '<':
            if not (actual_value < expected_value):
                return False
        elif operator == '>=':
            if not (actual_value >= expected_value):
                return False
        elif operator == '<=':
            if not (actual_value <= expected_value):
                return False
        elif operator == 'in':
            if not (actual_value in expected_value):
                return False
        elif operator == 'not in':
            if not (actual_value not in expected_value):
                return False
        else:
            raise ValueError(f"Unsupported operator: {operator}")
            
    return True

if __name__ == '__main__':
    vars_dict = {
        'x': 10,
        'y': 20,
        'z': 'hello'
    }
    
    conds = [
        ('x', '>', 5),
        ('y', '<', 25),
        ('z', 'in', ['hello', 'world']),
        ('x', '==', 10)
    ]
    
    result = evaluate_complex_logic(vars_dict, conds)
    print(result)