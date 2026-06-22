class TripleChecker:
    POSITIVE_THRESHOLD = 0
    EVEN_REMAINDER = 0

    def validate(self, a, b, c):
        is_positive_a = a > self.POSITIVE_THRESHOLD
        is_positive_b = b > self.POSITIVE_THRESHOLD
        is_positive_c = c > self.POSITIVE_THRESHOLD

        if not (is_positive_a and is_positive_b and is_positive_c):
            return False

        is_even_a = a % 2 == self.EVEN_REMAINDER
        is_even_b = b % 2 == self.EVEN_REMAINDER

        if not (is_even_a and is_even_b):
            return False

        sum_ab = a + b
        is_divisible = sum_ab % c == 0

        return is_divisible

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(4, 6, 5))
    print(checker.validate(2, 4, 3))
    print(checker.validate(-2, 4, 6))
    print(checker.validate(3, 4, 6))