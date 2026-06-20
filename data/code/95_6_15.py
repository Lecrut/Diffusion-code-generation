class AttributeChecker:
    def __init__(self, values):
        self.values = values

    def validate_a(self, value):
        return isinstance(value, int) and value > 0

    def validate_b(self, value):
        return isinstance(value, int) and value % 2 == 0

    def validate_c(self, value, divisor):
        return isinstance(value, int) and value % divisor == 0

    def check_attributes(self):
        a = self.values.get('a', 0)
        b = self.values.get('b', 0)
        c = self.values.get('c', 0)
        return (self.validate_a(a) and
                self.validate_b(b) and
                self.validate_c(c, a))

if __name__ == '__main__':
    checker = AttributeChecker({'a': 5, 'b': 4, 'c': 10})
    print(checker.check_attributes())