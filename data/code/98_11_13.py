def evaluate_complex_logic(variables, conditions):
    operators = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        'in': lambda a, b: a in b,
        'not_in': lambda a, b: a not in b,
    }
    for var_name, op, val in conditions:
        if var_name not in variables:
            return False
        actual_value = variables[var_name]
        if op not in operators:
            raise ValueError(f"Unsupported operator: {op}")
        if not operators[op](actual_value, val):
            return False
    return True

if __name__ == '__main__':
    vars_dict = {'x': 10, 'y': 'hello', 'z': [1, 2, 3]}
    conds = [('x', '>', 5), ('y', '==', 'hello'), ('z', 'in', [1, 2, 3, 4])]
    result = evaluate_complex_logic(vars_dict, conds)
    print(result)