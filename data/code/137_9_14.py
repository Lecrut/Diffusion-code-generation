class NumberClassifier:
    def classify(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or float")
        return "Positive" if value > 0 else "Negative" if value < 0 else "Zero"

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_values = [10, -25, 0, 3.14, -0.01]
    for val in sample_values:
        print(classifier.classify(val))