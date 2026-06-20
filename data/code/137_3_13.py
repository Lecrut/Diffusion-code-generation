class NumberClassifier:
    def classify(self, number: int) -> str:
        if number < 10:
            return "small"
        elif number < 100:
            return "medium"
        else:
            return "large"

if __name__ == '__main__':
    classifier = NumberClassifier()
    sample_numbers = [5, 45, 99, 100, 200]
    for num in sample_numbers:
        print(f"{num}: {classifier.classify(num)}")