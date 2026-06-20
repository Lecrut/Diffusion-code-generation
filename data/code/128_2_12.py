class NegativeNumberValidator:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    validator = NegativeNumberValidator()
    sample_values = [10, -5, 0, -100, 3.14, -0.001]
    for value in sample_values:
        result = validator.is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")