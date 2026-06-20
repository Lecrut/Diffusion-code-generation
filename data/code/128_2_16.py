class NegativeChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        result = NegativeChecker.is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")