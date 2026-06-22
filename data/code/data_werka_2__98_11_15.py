def evaluate_complex_logic(variables, conditions):
    if not conditions:
        return True
    op_map = {
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        'in': lambda x, y: x in y,
        'not in': lambda x, y: x not in y,
    }
    for name, op, target in conditions:
        if name not in variables:
            return False
        current_val = variables[name]
        checker = op_map.get(op)
        if checker is None:
            raise ValueError(f"Unsupported operator: {op}")
        if not checker(current_val, target):
            return False
    return True

if __name__ == '__main__':
    vars_dict = {
        'age': 25,
        'score': 85,
        'status': 'active'
    }
    req_conditions = [
        ('age', '>=', 18),
        ('score', '>', 80),
        ('status', '==', 'active')
    ]
    result = evaluate_complex_logic(vars_dict, req_conditions)
    print(result)