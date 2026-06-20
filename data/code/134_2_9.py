class ExclusiveConditionChecker:
    def __init__(self, condition1, condition2, condition3, condition4):
        self.conditions = (condition1, condition2, condition3, condition4)

    def is_exclusive(self):
        return sum(self.conditions) == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    print(checker.is_exclusive())