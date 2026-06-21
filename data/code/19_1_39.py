class ConditionChecker:
    def check_condition(self, a, b):
        return self._are_equal(a, b)

    def _are_equal(self, x, y):
        return x == y

if __name__ == '__main__':
    checker = ConditionChecker()
    value1 = 7
    value2 = 7
    result1 = checker.check_condition(value1, value2)
    print(result1)

    value3 = 15
    value4 = 30
    result2 = checker.check_condition(value3, value4)
    print(result2)