class MathUtils:
    @staticmethod
    def is_positive(number):
        if number > 0:
            return True
        return False

if __name__ == '__main__':
    test_values = [7, -3, 0, 2.5, -8]
    for value in test_values:
        print(f"{value} is positive: {MathUtils.is_positive(value)}")