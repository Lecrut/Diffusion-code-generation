class ConditionChecker:
    _MIN_VALUE = 0
    _MAX_VALUE = 100
    _REQUIRED_MODULUS = 2
    _REQUIRED_REMAINDER = 0
    _EXCLUDED_VALUE = 50

    @staticmethod
    def _is_positive(x):
        return x > ConditionChecker._MIN_VALUE

    @staticmethod
    def _is_less_than_max(x):
        return x < ConditionChecker._MAX_VALUE

    @staticmethod
    def _is_even(x):
        return x % ConditionChecker._REQUIRED_MODULUS == ConditionChecker._REQUIRED_REMAINDER

    @staticmethod
    def _is_not_excluded(x):
        return x != ConditionChecker._EXCLUDED_VALUE

    def check_all(self, value):
        results = [
            self._is_positive(value),
            self._is_less_than_max(value),
            self._is_even(value),
            self._is_not_excluded(value)
        ]
        return all(results)

if __name__ == '__main__':
    checker = ConditionChecker()
    val1 = 10
    val2 = 50
    val3 = 101
    val4 = -10
    print(checker.check_all(val1))
    print(checker.check_all(val2))
    print(checker.check_all(val3))
    print(checker.check_all(val4))