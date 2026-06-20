class NumberClassifier:

    def categorize(self, number):
        return 'Positive' if number > 0 else 'Negative' if number < 0 else 'Zero'
if __name__ == '__main__':
    classifier = NumberClassifier()
    print(classifier.categorize(10))
    print(classifier.categorize(-5))
    print(classifier.categorize(0))