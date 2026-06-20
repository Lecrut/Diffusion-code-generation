class ExclusiveConditionChecker:
    def __init__(self, cond1, cond2, cond3, cond4):
        self.conditions = [cond1, cond2, cond3, cond4]

    def is_exclusive(self):
        return sum(self.conditions) == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    print(checker.is_exclusive())