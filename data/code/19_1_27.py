class ConditionChecker:

    def check_condition(self, a, b):
        return self._compare(a, b)

    def _compare(self, a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(5, 3))
    print(checker.check_condition(-1, -1))
    print(checker.check_condition(0, 0))
    print(checker.check_condition(100, 200))