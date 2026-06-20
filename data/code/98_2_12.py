class ConditionChecker:

    def evaluate(self, conditions):
        for key, value in conditions.items():
            if not self._check_condition(key, value):
                return None
        return True

    def _check_condition(self, key, value):
        if key == 'greater_than_10':
            return value > 10
        elif key == 'less_than_5':
            return value < 5
        else:
            raise ValueError(f'Unknown condition: {key}')
if __name__ == '__main__':
    checker = ConditionChecker()
    conditions = {'greater_than_10': 12, 'less_than_5': 3}
    result = checker.evaluate(conditions)
    print(result)