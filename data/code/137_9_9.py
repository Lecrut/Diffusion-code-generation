class NumberClassifier:
    def classify(self, num):
        return 'positive' if num > 0 else 'negative' if num < 0 else 'zero'

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.classify(10))
    print(classifier.classify(-5))
    print(classifier.classify(0))