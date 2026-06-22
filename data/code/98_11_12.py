def evaluate_complex_logic(variables, conditions):
    COMPARISON_OPS = {
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
        current_val = variables[var_name]
        if op not in COMPARISON_OPS:
            raise ValueError(f"Unsupported operator: {op}")
        if not COMPARISON_OPS[op](current_val, val):
            return False
    return True

if __name__ == '__main__':
    sample_vars = {'x': 10, 'y': 'hello', 'z': [1, 2, 3]}
    sample_conds = [('x', '>', 5), ('y', '==', 'hello'), ('z', 'in', [1, 2, 3, 4])]
    result = evaluate_complex_logic(sample_vars, sample_conds)
    print(result)