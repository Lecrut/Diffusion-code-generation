class AttributeValidator:
    POSITIVE_THRESHOLD = 0
    EVEN_MODULUS = 2

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_a_positive(self):
        return self.a > self.POSITIVE_THRESHOLD

    def is_b_even(self):
        return self.b % self.EVEN_MODULUS == 0

    def is_c_divisible_by_a(self):
        if self.a == 0:
            return False
        return self.c % self.a == 0

    def validate_all(self):
        return self.is_a_positive() and self.is_b_even() and self.is_c_divisible_by_a()

if __name__ == '__main__':
    validator = AttributeValidator(3, 6, 12)
    print(validator.is_a_positive())
    print(validator.is_b_even())
    print(validator.is_c_divisible_by_a())
    print(validator.validate_all())