class AttributeValidator:
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

    def validate(self):
        return self._check_a_positive() and self._check_b_even() and self._check_c_divisible_by_a()

if __name__ == '__main__':
    validator = AttributeValidator(2, 4, 8)
    result = validator.validate()
    print(result)