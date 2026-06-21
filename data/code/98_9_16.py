MIN_LOWER_BOUND = 0
MAX_UPPER_BOUND = 100
EVEN_DIVISOR = 2
ODD_DIVISOR = 3

class ConditionChecker:
    def __init__(self):
        self._lower_bound = MIN_LOWER_BOUND
        self._upper_bound = MAX_UPPER_BOUND
        self._even_divisor = EVEN_DIVISOR
        self._odd_divisor = ODD_DIVISOR

    def _check_range(self, value):
        return value > self._lower_bound and value < self._upper_bound

    def _check_divisible_by_two(self, value):
        return value % self._even_divisor == 0

    def _check_divisible_by_three(self, value):
        return value % self._odd_divisor == 0

    def check_all(self, value):
        results = []
        results.append(self._check_range(value))
        results.append(self._check_divisible_by_two(value))
        results.append(self._check_divisible_by_three(value))
        return all(results)

if __name__ == '__main__':
    checker = ConditionChecker()
    val = 12
    outcome = checker.check_all(val)
    print(outcome)
    val_negative = -10
    outcome_neg = checker.check_all(val_negative)
    print(outcome_neg)