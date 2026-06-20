class TripleChecker:

    def validate(self, a, b, c):
        if self._is_positive(a) and self._is_positive(b) and self._is_positive(c):
            if self._is_even(a) and self._is_even(b):
                if self._sum_divisible_by_third(a, b, c):
                    return True
        return False

    def _is_positive(self, num):
        return num > 0

    def _is_even(self, num):
        return num % 2 == 0

    def _sum_divisible_by_third(self, a, b, c):
        return (a + b) % c == 0
if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))