def evaluate_complex_logic(variables, conditions):
    valid_ops = {
        'eq': lambda a, b: a == b,
        'ne': lambda a, b: a != b,
        'gt': lambda a, b: a > b,
        'lt': lambda a, b: a < b,
        'gte': lambda a, b: a >= b,
        'lte': lambda a, b: a <= b,
    }
    
    for item in conditions:
        if len(item) != 3:
            raise ValueError("Each condition must be a tuple of (variable_name, operator, value)")
        
        var_name, op_code, target_value = item
        
        if var_name not in variables:
            return False
            
        if op_code not in valid_ops:
            raise ValueError(f"Operator '{op_code}' is not supported.")
            
        current_value = variables[var_name]
        comparison_func = valid_ops[op_code]
        
        if not comparison_func(current_value, target_value):
            return False
            
    return True

if __name__ == '__main__':
    data = {
        'age': 25,
        'score': 95,
        'level': 3,
        'active': True
    }
    
    requirements = [
        ('age', 'gte', 18),
        ('score', 'gt', 90),
        ('level', 'lte', 5),
        ('active', 'eq', True)
    ]
    
    result = evaluate_complex_logic(data, requirements)
    print(result)