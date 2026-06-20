class Validator:
    MIN_VALUE = 0
    MAX_VALUE = 100

    @staticmethod
    def is_positive(number):
        return number > Validator.MIN_VALUE

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_less_than_max(number):
        return number < Validator.MAX_VALUE

    def combine_and_report(self, a, b, c):
        status = {
            'a': {'value': a, 'is_valid': self.is_positive(a) and self.is_even(a) and self.is_less_than_max(a)},
            'b': {'value': b, 'is_valid': self.is_positive(b) and self.is_even(b) and self.is_less_than_max(b)},
            'c': {'value': c, 'is_valid': self.is_positive(c) and self.is_even(c) and self.is_less_than_max(c)}
        }
        return status

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 25, 99)
    print(result)