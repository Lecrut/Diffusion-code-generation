class CombinedAttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _check_a_positive(self):
        return self.a > 0

    def _check_b_even(self):
        return self.b % 2 == 0

    def _check_c_divisible_by_a(self):
        if self.a == 0:
            return False
        return self.c % self.a == 0

    def evaluate(self):
        checks = {
            'a_positive': self._check_a_positive,
            'b_even': self._check_b_even,
            'c_divisible_by_a': self._check_c_divisible_by_a
        }
        return all(check() for check in checks.values())

if __name__ == '__main__':
    checker = CombinedAttributeChecker(3, 4, 12)
    result = checker.evaluate()
    print(result)