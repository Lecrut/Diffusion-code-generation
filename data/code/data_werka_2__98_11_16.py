class LogicEvaluator:
    OPERATORS = {
        'eq': lambda a, b: a == b,
        'neq': lambda a, b: a != b,
        'gt': lambda a, b: a > b,
        'lt': lambda a, b: a < b,
        'gte': lambda a, b: a >= b,
        'lte': lambda a, b: a <= b,
        'contains': lambda a, b: b in a,
        'not_contains': lambda a, b: b not in a,
    }

    @staticmethod
    def check_condition(variables, condition):
        var_name, op, target_value = condition
        if var_name not in variables:
            return False
        if op not in LogicEvaluator.OPERATORS:
            raise ValueError(f"Operator '{op}' is not supported.")
        actual_value = variables[var_name]
        return LogicEvaluator.OPERATORS[op](actual_value, target_value)

    @classmethod
    def evaluate_complex_logic(cls, variables, conditions):
        for condition in conditions:
            if not cls.check_condition(variables, condition):
                return False
        return True

if __name__ == '__main__':
    vars_dict = {
        'age': 25,
        'score': 85,
        'name': 'Alice',
        'tags': ['admin', 'user']
    }
    cond_list = [
        ('age', 'gte', 18),
        ('score', 'gt', 80),
        ('name', 'eq', 'Alice'),
        ('tags', 'contains', 'admin')
    ]
    result = LogicEvaluator.evaluate_complex_logic(vars_dict, cond_list)
    print(result)