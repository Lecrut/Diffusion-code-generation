class NumberClassifier:
    def __init__(self, value):
        self.value = value

    def classify(self):
        if self.value > 0:
            return "positive"
        if self.value < 0:
            return "negative"
        return "zero"

if __name__ == '__main__':
    classifier = NumberClassifier(7)
    print(classifier.classify())
    classifier.value = -3
    print(classifier.classify())
    classifier.value = 0
    print(classifier.classify())