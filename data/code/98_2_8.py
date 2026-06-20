class ConditionChecker:

    def evaluate(self, params):
        for key, value in params.items():
            if not self.check_condition(key, value):
                return None
        return True

    def check_condition(self, key, value):
        return value > 10
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.evaluate({'a': 5, 'b': 20})
    print(result)