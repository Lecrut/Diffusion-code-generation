class LogicEvaluator:
    SUPPORTED_OPS = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        'in': lambda a, b: a in b,
        'not_in': lambda a, b: a not in b,
        'is': lambda a, b: a is b,
        'is_not': lambda a, b: a is not b,
    }

    @staticmethod
    def get_operator(name):
        if name not in LogicEvaluator.SUPPORTED_OPS:
            raise ValueError(f"Unsupported operator: {name}")
        return LogicEvaluator.SUPPORTED_OPS[name]

def evaluate_complex_logic(variables, conditions):
    for var_name, op, val in conditions:
        if var_name not in variables:
            return False
        actual = variables[var_name]
        op_func = LogicEvaluator.get_operator(op)
        if not op_func(actual, val):
            return False
    return True

if __name__ == '__main__':
    vars_dict = {
        'x': 10,
        'y': 20,
        'name': 'Alice',
        'tags': ['admin', 'user']
    }
    
    req_conditions = [
        ('x', '>', 5),
        ('y', '==', 20),
        ('name', 'in', ['Alice', 'Bob']),
        ('tags', 'not_in', ['guest'])
    ]
    
    result = evaluate_complex_logic(vars_dict, req_conditions)
    print(result)