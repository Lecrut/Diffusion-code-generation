class NumberClassifier:
    def classify(self, number):
        if number > 0:
            return 'Positive'
        elif number < 0:
            return 'Negative'
        else:
            return 'Zero'

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_values = [1, -3, 0]
    for value in sample_values:
        print(classifier.classify(value))