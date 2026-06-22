class ConditionChecker:
    _MIN_VAL = 1
    _MAX_VAL = 100
    _REQUIRED_DIVISORS = (2, 3, 5)

    def __init__(self):
        self._min_val = self._MIN_VAL
        self._max_val = self._MAX_VAL
        self._divisors = tuple(self._REQUIRED_DIVISORS)

    def _is_in_range(self, value):
        return self._min_val <= value <= self._max_val

    def _is_divisible_by_all(self, value):
        for divisor in self._divisors:
            if value % divisor != 0:
                return False
        return True

    def check_all(self, value):
        if not self._is_in_range(value):
            return False
        if not self._is_divisible_by_all(value):
            return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all(30)
    print(result)
    result2 = checker.check_all(15)
    print(result2)
    result3 = checker.check_all(101)
    print(result3)
    result4 = checker.check_all(0)
    print(result4)