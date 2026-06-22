class ConditionChecker:
    MIN_POSITIVE = 1
    EVEN_STEP = 2

    @staticmethod
    def _validate_positive(value):
        return value >= ConditionChecker.MIN_POSITIVE

    @staticmethod
    def _validate_even(value):
        return value % ConditionChecker.EVEN_STEP == 0

    @staticmethod
    def _compute_product(first, second):
        return first * second

    @staticmethod
    def _check_divisibility(numerator, denominator):
        if denominator == 0:
            return False
        return numerator % denominator == 0

    def check(self, a, b, c):
        is_positive = self._validate_positive(a)
        is_even = self._validate_even(b)
        
        if not is_positive or not is_even:
            return False
        
        product = self._compute_product(a, b)
        return self._check_divisibility(c, product)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(3, 4, 12)
    print(result)