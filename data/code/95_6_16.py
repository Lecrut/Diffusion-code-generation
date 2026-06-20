class AttributeChecker:
    def __init__(self, values):
        self.values = values

    def is_positive(self, value):
        return isinstance(value, int) and value > 0

    def is_even(self, value):
        return isinstance(value, int) and value % 2 == 0

    def is_divisible(self, dividend, divisor):
        return isinstance(dividend, int) and isinstance(divisor, int) and dividend % divisor == 0

    def check_attributes(self):
        a = self.values.get('a', 0)
        b = self.values.get('b', 0)
        c = self.values.get('c', 0)

        if not (self.is_positive(a) and self.is_even(b) and self.is_divisible(c, a)):
            raise ValueError("Invalid attributes: a must be positive, b must be even, and c must be divisible by a")

        return True

if __name__ == '__main__':
    checker = AttributeChecker({'a': 5, 'b': 4, 'c': 10})
    print(checker.check_attributes())