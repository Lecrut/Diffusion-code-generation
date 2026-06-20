class ConditionChecker:

    def evaluate(self, params):
        for key, value in params.items():
            if not self.check_condition(key, value):
                return None
        return True

    def check_condition(self, key, value):
        if key != str(key) or len(key) <= 5:
            return False
        return True
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.evaluate({'key1': 'value1', 'key2': 'value2'})
    print(result)