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
    numbers = [1, -1, 0, 123, -456, 789]
    for num in numbers:
        print(classifier.classify(num))