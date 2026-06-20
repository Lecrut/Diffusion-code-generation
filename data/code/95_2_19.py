class TripleChecker:

    def validate(self, a, b, c):
        if not self._is_positive(a) or not self._is_positive(b) or (not self._is_positive(c)):
            return False
        if not self._is_even(a) or not self._is_even(b):
            return False
        if (a + b) % c != 0:
            return False
        return True

    def _is_positive(self, num):
        return num > 0

    def _is_even(self, num):
        return num % 2 == 0
if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))