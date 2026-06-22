class ConditionChecker:
    def __init__(self):
        self._threshold = 10
        self._multiplier = 2
        self._offset = 5

    def _check_positive(self, value):
        return value > 0

    def _check_within_range(self, value):
        lower = 0
        upper = self._threshold * self._multiplier
        return lower < value < upper

    def _check_divisible(self, value):
        return value % self._offset == 0

    def check_all(self, value):
        res1 = self._check_positive(value)
        res2 = self._check_within_range(value)
        res3 = self._check_divisible(value)
        return res1 and res2 and res3

if __name__ == '__main__':
    checker = ConditionChecker()
    sample_value = 10
    outcome = checker.check_all(sample_value)
    print(outcome)
    sample_value_2 = 15
    outcome_2 = checker.check_all(sample_value_2)
    print(outcome_2)