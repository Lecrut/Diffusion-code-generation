class MathUtils:
    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    test_values = [-1, 2, -3.5, 4.2, 0]
    for value in test_values:
        print(f"{value} is positive: {MathUtils.is_positive(value)}")