class NumberClassifier:
    def classify(self, num):
        return 'Positive' if num > 0 else ('Negative' if num < 0 else 'Zero')

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_values = [-1, 0, 1]
    results = [classifier.classify(val) for val in sample_values]
    print(results)