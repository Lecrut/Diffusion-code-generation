class AttributeChecker:
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

    def check_attributes(self):
        return self.is_positive() and self.is_even() and self.is_divisible_by_a()

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.check_attributes())