class ConditionChecker:
    MINIMUM_THRESHOLD = 0
    MAXIMUM_THRESHOLD = 100
    DIVISOR_TWO = 2
    DIVISOR_THREE = 3

    def __init__(self):
        self.min_val = self.MINIMUM_THRESHOLD
        self.max_val = self.MAXIMUM_THRESHOLD
        self.mod_two = self.DIVISOR_TWO
        self.mod_three = self.DIVISOR_THREE

    def _check_lower_bound(self, value):
        return value > self.min_val

    def _check_upper_bound(self, value):
        return value < self.max_val

    def _check_even(self, value):
        return value % self.mod_two == 0

    def _check_divisible_by_three(self, value):
        return value % self.mod_three == 0

    def check_all(self, value):
        results = [
            self._check_lower_bound(value),
            self._check_upper_bound(value),
            self._check_even(value),
            self._check_divisible_by_three(value),
        ]
        for res in results:
            if not res:
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all(6))
    print(checker.check_all(12))
    print(checker.check_all(100))
    print(checker.check_all(-1))