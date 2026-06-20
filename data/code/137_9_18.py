class NumberClassifier:
    def classify(self, num):
        return 'Positive' if num > 0 else ('Negative' if num < 0 else 'Zero')

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_numbers = [1, -2, 0, 345, -6789]
    categorized = [classifier.classify(num) for num in sample_numbers]
    print(categorized)