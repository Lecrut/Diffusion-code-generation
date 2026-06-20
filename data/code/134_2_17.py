class ExclusiveConditionChecker:
    def __init__(self, cond1, cond2, cond3, cond4):
        self.conditions = [cond1, cond2, cond3, cond4]

    def is_exclusive(self):
        xor_result = 0
        for condition in self.conditions:
            xor_result ^= int(condition)
        return xor_result == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    result = checker.is_exclusive()
    print(result)