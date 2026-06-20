class LogicEvaluator:
    @staticmethod
    def evaluate_condition(variables, condition):
        var_name, operator, value = condition
        if operator == '==':
            return variables[var_name] == value
        elif operator == '<':
            return variables[var_name] < value
        elif operator == '>':
            return variables[var_name] > value
        elif operator == '<=':
            return variables[var_name] <= value
        elif operator == '>=':
            return variables[var_name] >= value
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    @staticmethod
    def evaluate_complex_logic(variables, conditions):
        for condition in conditions:
            if not LogicEvaluator.evaluate_condition(variables, condition):
                return False
        return True

if __name__ == '__main__':
    variables = {
        'age': 25,
        'access_level': "premium",
        'subscription_status': True
    }
    conditions = [
        ('age', '>=', 18),
        ('access_level', '==', "premium"),
        ('subscription_status', '==', True)
    ]
    result = LogicEvaluator.evaluate_complex_logic(variables, conditions)
    print(result)