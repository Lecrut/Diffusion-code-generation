class NumberCategorizer:
    LOW_LIMIT = 0
    MEDIUM_LIMIT = 100
    HIGH_LIMIT = 1000

    def __init__(self, low_limit=LOW_LIMIT, medium_limit=MEDIUM_LIMIT, high_limit=HIGH_LIMIT):
        self.low_limit = low_limit
        self.medium_limit = medium_limit
        self.high_limit = high_limit

    def categorize(self, value):
        if value < self.low_limit:
            return 'very_low'
        elif value < self.medium_limit:
            return 'low'
        elif value < self.high_limit:
            return 'medium'
        else:
            return 'high'

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    print(categorizer.categorize(50))
    print(categorizer.categorize(150))
    print(categorizer.categorize(500))
    print(categorizer.categorize(1500))
    print(categorizer.categorize(-10))