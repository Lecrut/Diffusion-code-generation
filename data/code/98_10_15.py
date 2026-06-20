class ConditionChecker:
    def __init__(self, conditions):
        self.conditions = conditions

    def check_all(self):
        return all(condition() for condition in self.conditions)

if __name__ == '__main__':
    conditions = [
        lambda: True,
        lambda: False,
        lambda: 1 == 1
    ]
    checker = ConditionChecker(conditions)
    print(checker.check_all())