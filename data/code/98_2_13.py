class ConditionChecker:

    def evaluate(self, conditions):
        for key, value in conditions.items():
            if not self.check_condition(key, value):
                return None
        return True

    def check_condition(self, key, value):
        if isinstance(value, int) and len(key) == value:
            return True
        return False
if __name__ == '__main__':
    checker = ConditionChecker()
    conditions = {'hello': 5, 'world': 5}
    result = checker.evaluate(conditions)
    print(result)