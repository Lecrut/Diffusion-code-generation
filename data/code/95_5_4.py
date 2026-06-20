class IntegerValidator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_positive(self):
        return self.a > 0

    def is_even(self):
        return self.b % 2 == 0

    def is_divisible_by_a(self):
        return self.c % self.a == 0

if __name__ == '__main__':
    validator = IntegerValidator(13, 24, 65)
    print(validator.is_positive())
    print(validator.is_even())
    print(validator.is_divisible_by_a())