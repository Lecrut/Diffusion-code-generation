class NumberAnalyzer:
    NEGATIVE_THRESHOLD = 0

    @staticmethod
    def is_negative(x):
        return x < NumberAnalyzer.NEGATIVE_THRESHOLD

if __name__ == '__main__':
    print(NumberAnalyzer.is_negative(-10))
    print(NumberAnalyzer.is_negative(0))
    print(NumberAnalyzer.is_negative(5))