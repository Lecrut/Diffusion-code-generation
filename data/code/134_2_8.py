class ExclusiveConditionChecker:
    def __init__(self, a, b, c, d):
        self.conditions = (a, b, c, d)

    def is_exclusive(self):
        return sum(self.conditions) == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    print(checker.is_exclusive())