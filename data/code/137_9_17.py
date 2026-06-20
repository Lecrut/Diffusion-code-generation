class NumberClassifier:

    def classify(self, number):
        return 'Positive' if number > 0 else 'Negative' if number < 0 else 'Zero'
if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.classify(10))
    print(classifier.classify(-5))
    print(classifier.classify(0))