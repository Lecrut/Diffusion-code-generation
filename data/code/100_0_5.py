class NumberClassifier:
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    ZERO = 'Zero'

    @staticmethod
    def classify_number(num):
        if num > 0:
            return NumberClassifier.POSITIVE
        elif num < 0:
            return NumberClassifier.NEGATIVE
        else:
            return NumberClassifier.ZERO

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.classify_number(3))
    print(classifier.classify_number(-2))
    print(classifier.classify_number(0))