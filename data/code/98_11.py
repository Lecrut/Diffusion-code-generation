class ConditionChecker:
    def __init__(self, conditions):
        self.conditions = conditions
    def check_all(self):
        result = True
        for condition in self.conditions:
            if not condition:
                result = False
                break
        return result
if __name__ == '__main__':
    sample_conditions = [True, False, True, True]
    checker = ConditionChecker(sample_conditions)
    result = checker.check_all()
    print(result)