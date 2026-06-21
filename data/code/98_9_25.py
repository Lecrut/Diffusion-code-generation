class ConditionChecker:
    MIN_VALUE = 0
    MAX_VALUE = 100
    DIVISOR_TWO = 2
    DIVISOR_THREE = 3
    EXCLUSION_VALUE = 50

    def __init__(self):
        self._threshold_min = self.MIN_VALUE
        self._threshold_max = self.MAX_VALUE
        self._divisor_2 = self.DIVISOR_TWO
        self._divisor_3 = self.DIVISOR_THREE
        self._exclusion = self.EXCLUSION_VALUE

    def _is_positive(self, value):
        return value > self._threshold_min

    def _is_within_range(self, value):
        return value < self._threshold_max

    def _is_even(self, value):
        return value % self._divisor_2 == 0

    def _is_divisible_by_three(self, value):
        return value % self._divisor_3 == 0

    def _is_not_excluded(self, value):
        return value != self._exclusion

    def check_all(self, value):
        results = [
            self._is_positive(value),
            self._is_within_range(value),
            self._is_even(value),
            self._is_divisible_by_three(value),
            self._is_not_excluded(value)
        ]
        return all(results)

if __name__ == '__main__':
    checker = ConditionChecker()
    val1 = 12
    print(checker.check_all(val1))
    val2 = 50
    print(checker.check_all(val2))
    val3 = 6
    print(checker.check_all(val3))
    val4 = 100
    print(checker.check_all(val4))