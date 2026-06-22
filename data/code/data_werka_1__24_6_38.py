class NumberAnalyzer:
    NEGATIVE_MESSAGE = "The entered value {} is negative."
    NON_NEGATIVE_MESSAGE = "The entered value {} is not negative."

    @staticmethod
    def analyze(number):
        if number < 0:
            return NumberAnalyzer.NEGATIVE_MESSAGE.format(number)
        else:
            return NumberAnalyzer.NON_NEGATIVE_MESSAGE.format(number)

if __name__ == '__main__':
    sample_values = [-5, 0, 15]
    for value in sample_values:
        print(NumberAnalyzer.analyze(value))