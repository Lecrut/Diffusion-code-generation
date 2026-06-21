class ConditionChecker:
    _CONDITIONS = (
        lambda v: v > 0,
        lambda v: v < 100,
        lambda v: v % 2 == 0,
    )

    @staticmethod
    def _evaluate(condition, value):
        return condition(value)

    def __init__(self):
        self.conditions = ConditionChecker._CONDITIONS

    def check_all(self, value):
        results = []
        for condition in self.conditions:
            if not self._evaluate(condition, value):
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    val1 = 42
    res1 = checker.check_all(val1)
    print(res1)
    val2 = -10
    res2 = checker.check_all(val2)
    print(res2)
    val3 = 101
    res3 = checker.check_all(val3)
    print(res3)