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
    conditions_data = [
        (10 > 5, True),
        (20 == 20, True),
        (5 < 10, True),
        (100 > 500, False)
    ]
    checker = ConditionChecker(conditions_data)
    result = checker.check_all()
    print(result)