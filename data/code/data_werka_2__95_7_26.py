class ConditionChecker:
    POSITIVE_THRESHOLD = 0
    EVEN_MODULUS = 2

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _is_positive(self, value):
        return value > self.POSITIVE_THRESHOLD

    def _is_even(self, value):
        return value % self.EVEN_MODULUS == 0

    def _is_divisible_by_product(self, dividend, divisor1, divisor2):
        product = divisor1 * divisor2
        if product == 0:
            return False
        return dividend % product == 0

    def evaluate(self):
        if not self._is_positive(self.a):
            return False
        if not self._is_even(self.b):
            return False
        return self._is_divisible_by_product(self.c, self.a, self.b)

if __name__ == '__main__':
    checker = ConditionChecker(3, 4, 12)
    result = checker.evaluate()
    print(result)