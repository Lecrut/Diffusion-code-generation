class ConditionChecker:

    def evaluate(self, params):
        for key, value in params.items():
            if not self.check_condition(key, value):
                return None
        return True

    def check_condition(self, key, value):
        if isinstance(value, dict):
            return all((self.check_condition(sub_key, sub_value) for sub_key, sub_value in value.items()))
        elif callable(value):
            return value()
        else:
            return key == value
if __name__ == '__main__':
    checker = ConditionChecker()
    params1 = {'a': 'a', 'b': {'c': 'c'}}
    print(checker.evaluate(params1))
    params2 = {'a': 'a', 'b': {'c': 'd'}}
    print(checker.evaluate(params2))