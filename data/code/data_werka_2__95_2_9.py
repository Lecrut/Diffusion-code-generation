class TripleChecker:
    POSITIVE_THRESHOLD = 0
    DIVISOR_MIN = 1

    def validate(self, a, b, c):
        self._check_validity(a, b, c)
        is_even_a = a % 2 == 0
        is_even_b = b % 2 == 0
        is_sum_divisible = (a + b) % c == 0
        return is_even_a and is_even_b and is_sum_divisible

    def _check_validity(self, a, b, c):
        if a <= self.POSITIVE_THRESHOLD:
            raise ValueError("First number must be positive")
        if b <= self.POSITIVE_THRESHOLD:
            raise ValueError("Second number must be positive")
        if c <= self.POSITIVE_THRESHOLD:
            raise ValueError("Third number must be positive")
        if c == 0:
            raise ValueError("Third number cannot be zero for division")

if __name__ == '__main__':
    checker = TripleChecker()
    result1 = checker.validate(2, 4, 6)
    print(result1)
    result2 = checker.validate(1, 2, 3)
    print(result2)
    result3 = checker.validate(2, 2, 5)
    print(result3)
    result4 = checker.validate(3, 4, 6)
    print(result4)
    result5 = checker.validate(10, 20, 30)
    print(result5)
    result6 = checker.validate(4, 8, 12)
    print(result6)