class MathUtils:
    POSITIVE_THRESHOLD = 0

    @staticmethod
    def is_positive(number):
        return number > MathUtils.POSITIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [15, -3, 0, 7.89, -6.28]
    for value in sample_values:
        print(f"{value} is positive: {MathUtils.is_positive(value)}")