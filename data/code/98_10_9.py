class ConditionChecker:
    def __init__(self, conditions):
        self.conditions = conditions

    def check_all(self):
        return all(self.conditions)

if __name__ == '__main__':
    conditions = [True, False, True]
    checker = ConditionChecker(conditions)
    result = checker.check_all()
    print(f"Conditions: {conditions}")
    print(f"All conditions met: {result}")