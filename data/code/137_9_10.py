class NumberClassifier:
    def classify(self, value):
        return "positive" if value > 0 else ("negative" if value < 0 else "zero")

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.classify(5))
    print(classifier.classify(-3))
    print(classifier.classify(0))