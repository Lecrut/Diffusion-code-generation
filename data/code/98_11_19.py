def evaluate_complex_logic(variables, conditions):
    if not isinstance(variables, dict):
        raise TypeError("variables must be a dictionary")
    if not isinstance(conditions, (list, tuple)):
        raise TypeError("conditions must be a list of tuples")
    
    op_map = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        'in': lambda a, b: a in b,
        'not_in': lambda a, b: a not in b,
    }

    def check_condition(var_name, operator, target_value):
        if var_name not in variables:
            return False
        if operator not in op_map:
            raise ValueError(f"Operator '{operator}' is not supported")
        
        source_value = variables[var_name]
        logic_func = op_map[operator]
        return logic_func(source_value, target_value)

    result = True
    for condition in conditions:
        if not check_condition(*condition):
            result = False
            break
    return result

if __name__ == '__main__':
    test_vars = {
        'x': 10,
        'y': 'hello',
        'z': [1, 2, 3],
        'flag': True
    }
    
    test_conds = [
        ('x', '>', 5),
        ('y', '==', 'hello'),
        ('z', 'in', [1, 2, 3, 4]),
        ('flag', '==', True)
    ]
    
    all_met = evaluate_complex_logic(test_vars, test_conds)
    print(all_met)
    
    test_conds_fail = [
        ('x', '>', 10),
        ('y', '==', 'hello')
    ]
    
    all_met_fail = evaluate_complex_logic(test_vars, test_conds_fail)
    print(all_met_fail)
    
    test_conds_unsupported = [
        ('x', '**', 2)
    ]
    
    try:
        evaluate_complex_logic(test_vars, test_conds_unsupported)
    except ValueError as e:
        print(str(e))