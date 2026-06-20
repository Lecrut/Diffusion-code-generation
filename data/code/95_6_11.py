class AttributeValidator:
    def __init__(self, values):
        self.values = values

    def is_positive(self, value):
        return isinstance(value, int) and value > 0

    def is_even(self, value):
        return isinstance(value, int) and value % 2 == 0

    def is_divisible(self, dividend, divisor):
        return isinstance(dividend, int) and isinstance(divisor, int) and divisor != 0 and dividend % divisor == 0

    def validate_attributes(self):
        a = self.values.get('a', None)
        b = self.values.get('b', None)
        c = self.values.get('c', None)

        if not self.is_positive(a):
            raise ValueError("Attribute 'a' must be a positive integer")
        if not self.is_even(b):
            raise ValueError("Attribute 'b' must be an even integer")
        if not self.is_divisible(c, a):
            raise ValueError("Attribute 'c' must be divisible by 'a'")

        return True

if __name__ == '__main__':
    validator = AttributeValidator({'a': 5, 'b': 4, 'c': 10})
    try:
        result = validator.validate_attributes()
        print(result)
    except ValueError as e:
        print(e)