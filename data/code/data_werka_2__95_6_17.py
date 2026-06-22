class TripleValidator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _verify_positive(self, value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")
        return True

    def _verify_even(self, value, name):
        if value % 2 != 0:
            raise ValueError(f"{name} must be even, got {value}")
        return True

    def _verify_divisible(self, numerator, denominator, name):
        if denominator == 0:
            raise ValueError(f"{name} cannot be zero for division")
        if numerator % denominator != 0:
            raise ValueError(f"{name} is not divisible by {denominator}")
        return True

    def run_checks(self):
        self._verify_positive(self.a, 'a')
        self._verify_even(self.b, 'b')
        self._verify_divisible(self.c, self.a, 'c')
        return True

if __name__ == '__main__':
    validator = TripleValidator(2, 4, 10)
    outcome = validator.run_checks()
    print(outcome)