class ConditionChecker:

    def check_condition(self, a, b):
        return self._are_equal(a, b)

    def _are_equal(self, x, y):
        return x == y
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(3, 7))
    print(checker.check_condition(42, 42))
    print(checker.check_condition(-1, 0))