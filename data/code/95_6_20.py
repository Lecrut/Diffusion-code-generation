class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_positive(self, value):
        return value > 0

    def is_even(self, value):
        return value % 2 == 0

    def is_divisible(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")
        return dividend % divisor == 0

    def check_attributes(self):
        if not self.is_positive(self.a):
            raise ValueError("a must be a positive integer")
        if not self.is_even(self.b):
            raise ValueError("b must be an even integer")
        try:
            if not self.is_divisible(self.c, self.a):
                raise ValueError("c must be divisible by a")
        except ValueError as e:
            print(e)
            return False
        return True

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.check_attributes())