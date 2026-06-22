class ConditionChecker:
    FIRST_POSITIVE = 0
    SECOND_EVEN = 1
    THIRD_DIVISIBLE = 2

    @staticmethod
    def _validate_positive(value):
        return value > 0

    @staticmethod
    def _validate_even(value):
        return value % 2 == 0

    @staticmethod
    def _validate_divisible(dividend, divisor):
        if divisor == 0:
            return False
        return dividend % divisor == 0

    def check(self, a, b, c):
        is_first_positive = self._validate_positive(a)
        if not is_first_positive:
            return False
        is_second_even = self._validate_even(b)
        if not is_second_even:
            return False
        product = a * b
        is_third_divisible = self._validate_divisible(c, product)
        return is_third_divisible

if __name__ == '__main__':
    checker = ConditionChecker()
    val_a = 3
    val_b = 4
    val_c = 12
    result = checker.check(val_a, val_b, val_c)
    print(result)