class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_positive(self, value):
        return value > 0

    def check_even(self, value):
        return value % 2 == 0

    def check_divisibility(self, dividend, divisor):
        return dividend % divisor == 0

    def check_attributes(self):
        return (self.check_positive(self.a) and
                self.check_even(self.b) and
                self.check_divisibility(self.c, self.a))

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.check_attributes())