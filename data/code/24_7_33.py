class MathUtils:
    NEGATIVE_THRESHOLD = 0

    @staticmethod
    def is_negative(number):
        return number < MathUtils.NEGATIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [-1, 2, -3.5, 4, 0]
    for value in sample_values:
        print(f"{value} is negative: {MathUtils.is_negative(value)}")