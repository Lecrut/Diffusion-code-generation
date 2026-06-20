class NumberClassifier:
    def classify(self, num):
        return "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_numbers = [1, -5, 0, 34]
    categorized_numbers = [classifier.classify(n) for n in sample_numbers]
    print(categorized_numbers)