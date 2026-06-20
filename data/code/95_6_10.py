class AttributeChecker:
    def __init__(self, values):
        self.values = values

    def is_positive(self, value):
        return value > 0

    def is_even(self, value):
        return value % 2 == 0

    def is_divisible(self, dividend, divisor):
        return dividend % divisor == 0

    def check_attributes(self):
        a = self.values.get('a', 0)
        b = self.values.get('b', 0)
        c = self.values.get('c', 0)
        return (self.is_positive(a) and
                self.is_even(b) and
                self.is_divisible(c, a))

if __name__ == '__main__':
    checker = AttributeChecker({'a': 5, 'b': 4, 'c': 10})
    print(checker.check_attributes())