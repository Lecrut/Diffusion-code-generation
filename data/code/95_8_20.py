class NumberValidator:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number")
        self.value = value

    def is_positive(self):
        return self.value > 0

    def is_even(self):
        return self.value % 2 == 0

    def is_less_than_100(self):
        return self.value < 100

    def check(self):
        if not self.is_positive():
            return "Not positive"
        if not self.is_even():
            return "Odd"
        if not self.is_less_than_100():
            return "Too large"
        return "Positive, even, and less than 100"

if __name__ == '__main__':
    samples = [50, -5, 7, 101, 42.0]
    for s in samples:
        validator = NumberValidator(s)
        print(validator.check())