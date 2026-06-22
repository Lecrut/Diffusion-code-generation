class NumberCategorizer:
    def __init__(self, low_threshold=10, medium_threshold=50):
        self.low_threshold = low_threshold
        self.medium_threshold = medium_threshold

    def categorize(self, value):
        if value < self.low_threshold:
            return 'low'
        if value < self.medium_threshold:
            return 'medium'
        return 'high'

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    print(categorizer.categorize(5))
    print(categorizer.categorize(35))
    print(categorizer.categorize(100))
    print(categorizer.categorize(9))
    print(categorizer.categorize(50))
    print(categorizer.categorize(101))