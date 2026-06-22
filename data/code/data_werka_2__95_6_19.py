class TripleConditionChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _ensure_positive(self, value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return value

    def _ensure_even(self, value, name):
        if value % 2 != 0:
            raise ValueError(f"{name} must be even")
        return value

    def _ensure_divisible(self, dividend, divisor, div_name):
        if dividend % divisor != 0:
            raise ValueError(f"{dividend} is not divisible by {divisor}")
        return True

    def check_all(self):
        self._ensure_positive(self.a, 'a')
        self._ensure_even(self.b, 'b')
        self._ensure_divisible(self.c, self.a, 'c')
        return True

if __name__ == '__main__':
    checker = TripleConditionChecker(4, 6, 12)
    result = checker.check_all()
    print(result)