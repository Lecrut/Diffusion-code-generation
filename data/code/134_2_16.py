class ExclusiveConditionChecker:
    def __init__(self, condition1, condition2, condition3, condition4):
        self.conditions = [condition1, condition2, condition3, condition4]

    @staticmethod
    def is_exclusive(conditions):
        return sum(conditions) == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    result = checker.is_exclusive(checker.conditions)
    print(result)