class NumberClassifier:
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    ZERO = 'Zero'

    @staticmethod
    def classify(num):
        if num > 0:
            return NumberClassifier.POSITIVE
        elif num < 0:
            return NumberClassifier.NEGATIVE
        else:
            return NumberClassifier.ZERO

if __name__ == '__main__':
    print(NumberClassifier.classify(3))
    print(NumberClassifier.classify(-2))
    print(NumberClassifier.classify(0))