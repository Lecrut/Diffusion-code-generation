class NumberClassifier:
    SMALL = 10
    MEDIUM = 50

    @staticmethod
    def classify(number: int) -> str:
        if number < NumberClassifier.SMALL:
            return 'small'
        elif number <= NumberClassifier.MEDIUM:
            return 'medium'
        else:
            return 'large'

if __name__ == '__main__':
    sample_number = 35
    category = NumberClassifier.classify(sample_number)
    print(f"{sample_number}: {category}")