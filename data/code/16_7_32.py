class MathUtils:
    POSITIVITY_THRESHOLD = 0

    @staticmethod
    def is_positive(number):
        return number > MathUtils.POSITIVITY_THRESHOLD

if __name__ == '__main__':
    sample_values = [7, -3, 0, 2.5, -1.2]
    results = {value: MathUtils.is_positive(value) for value in sample_values}
    print(results)