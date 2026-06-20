class ExclusiveConditionChecker:

    def __init__(self, cond1, cond2, cond3, cond4):
        self.conditions = [cond1, cond2, cond3, cond4]

    def is_exclusive(self):
        return self.conditions[0] ^ self.conditions[1] ^ self.conditions[2] ^ self.conditions[3] == 3
if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    result = checker.is_exclusive()
    print(result)