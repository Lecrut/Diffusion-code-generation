class MathUtils:
    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    test_values = [7, -3, 0, 15.5, -8.2]
    for value in test_values:
        result = MathUtils.is_positive(value)
        print(f"The number {value} is positive: {result}")