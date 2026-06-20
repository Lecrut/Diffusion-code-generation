class ExclusiveConditionChecker:
    def __init__(self, cond1, cond2, cond3, cond4):
        self.conditions = [cond1, cond2, cond3, cond4]

    @staticmethod
    def is_exclusive(conditions):
        return bool(sum(int(cond) for cond in conditions) & (sum(int(cond) for cond in conditions) - 1))

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    result = ExclusiveConditionChecker.is_exclusive(checker.conditions)
    print(result)