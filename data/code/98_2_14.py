class ConditionChecker:

    def evaluate(self, params):
        for key, value in params.items():
            if not self.check_condition(key, value):
                return None
        return True

    def check_condition(self, key, value):
        if isinstance(value, str) and len(value) > 5:
            return True
        return False
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.evaluate({'name': 'Alice', 'age': 30})
    print(result)