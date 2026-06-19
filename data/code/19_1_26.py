class ConditionChecker:

    def check_condition(self, a, b):
        return self._are_equal(a, b)

    @staticmethod
    def _are_equal(x, y):
        return x == y
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(5, 3))
    print(checker.check_condition(-1, -1))
    print(checker.check_condition(0, 0))