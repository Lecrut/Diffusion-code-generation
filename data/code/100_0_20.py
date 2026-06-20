class NumberClassifier:
    def classify(self, num):
        if num > 0:
            return 'Positive'
        elif num < 0:
            return 'Negative'
        else:
            return 'Zero'

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.classify(3))
    print(classifier.classify(-2))
    print(classifier.classify(0))