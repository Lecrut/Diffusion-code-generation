class NumberClassifier:
    def classify(self, number):
        return "Positive" if number > 0 else "Negative" if number < 0 else "Zero"

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_values = [10, -5, 0, 3.14, -2.71]
    for value in sample_values:
        print(f"{value}: {classifier.classify(value)}")