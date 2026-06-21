class ConditionChecker:
    def check_condition(self, a, b):
        return self._compare(a, b)

    def _compare(self, x, y):
        return x == y

if __name__ == '__main__':
    CHECKER = ConditionChecker()
    SAMPLE_VALUE_1 = 7
    SAMPLE_VALUE_2 = 7
    SAMPLE_VALUE_3 = 15
    print(CHECKER.check_condition(SAMPLE_VALUE_1, SAMPLE_VALUE_2))
    print(CHECKER.check_condition(SAMPLE_VALUE_1, SAMPLE_VALUE_3))