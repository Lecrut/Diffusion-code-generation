class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_positive(self, value):
        return isinstance(value, int) and value > 0

    def is_even(self, value):
        return isinstance(value, int) and value % 2 == 0

    def is_divisible(self, dividend, divisor):
        return isinstance(dividend, int) and isinstance(divisor, int) and dividend % divisor == 0

    def check_attributes(self):
        if not self.is_positive(self.a):
            raise ValueError("a must be a positive integer")
        if not self.is_even(self.b):
            raise ValueError("b must be an even integer")
        if not self.is_divisible(self.c, self.a):
            raise ValueError("c must be divisible by a")
        return True

if __name__ == '__main__':
    try:
        checker = AttributeChecker(5, 4, 10)
        print(checker.check_attributes())
    except ValueError as e:
        print(e)