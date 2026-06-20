class ExclusiveConditionChecker:
    def __init__(self, condition1, condition2, condition3, condition4):
        self.conditions = (condition1, condition2, condition3, condition4)

    def is_exclusive(self):
        combined = sum(2 ** i if cond else 0 for i, cond in enumerate(self.conditions))
        return combined & (combined - 1) == 0 and combined != 0

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    result = checker.is_exclusive()
    print(result)