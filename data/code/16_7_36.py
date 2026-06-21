class MathUtils:
    POSITIVITY_THRESHOLD = 0

    @staticmethod
    def is_positive(number):
        return number > MathUtils.POSITIVITY_THRESHOLD

if __name__ == '__main__':
    sample_values = [7, -3, 0, 1.618, -0.577]
    for value in sample_values:
        print(f"{value} is positive: {MathUtils.is_positive(value)}")