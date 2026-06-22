def evaluate_complex_logic(variables, conditions):
    OP_EQUAL = '=='
    OP_NOT_EQUAL = '!='
    OP_GREATER = '>'
    OP_LESS = '<'
    OP_GREATER_EQUAL = '>='
    OP_LESS_EQUAL = '<='
    OP_IN = 'in'
    OP_NOT_IN = 'not in'

    SUPPORTED_OPERATORS = frozenset([
        OP_EQUAL,
        OP_NOT_EQUAL,
        OP_GREATER,
        OP_LESS,
        OP_GREATER_EQUAL,
        OP_LESS_EQUAL,
        OP_IN,
        OP_NOT_IN
    ])

    def check_equality(a, b):
        return a == b

    def check_inequality(a, b):
        return a != b

    def check_greater(a, b):
        return a > b

    def check_less(a, b):
        return a < b

    def check_greater_equal(a, b):
        return a >= b

    def check_less_equal(a, b):
        return a <= b

    def check_in(a, b):
        return a in b

    def check_not_in(a, b):
        return a not in b

    OPERATION_MAP = {
        OP_EQUAL: check_equality,
        OP_NOT_EQUAL: check_inequality,
        OP_GREATER: check_greater,
        OP_LESS: check_less,
        OP_GREATER_EQUAL: check_greater_equal,
        OP_LESS_EQUAL: check_less_equal,
        OP_IN: check_in,
        OP_NOT_IN: check_not_in,
    }

    for condition in conditions:
        var_name, operator, expected_value = condition
        
        if operator not in SUPPORTED_OPERATORS:
            raise ValueError(f"Unsupported operator: {operator}")
        
        if var_name not in variables:
            return False
        
        current_value = variables[var_name]
        
        operation_func = OPERATION_MAP[operator]
        if not operation_func(current_value, expected_value):
            return False
            
    return True

if __name__ == '__main__':
    sample_vars = {
        'x': 10,
        'y': 20,
        'name': 'test'
    }
    
    sample_conds = [
        ('x', '>', 5),
        ('y', '<', 25),
        ('name', '==', 'test'),
        ('x', '!=', 15)
    ]
    
    result = evaluate_complex_logic(sample_vars, sample_conds)
    print(result)