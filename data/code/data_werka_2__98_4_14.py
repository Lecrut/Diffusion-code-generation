class NumberCategorizer:
    LOW_LIMIT = 10
    MEDIUM_LIMIT = 50

    @staticmethod
    def categorize(n):
        if n < NumberCategorizer.LOW_LIMIT:
            return 'low'
        if n < NumberCategorizer.MEDIUM_LIMIT:
            return 'medium'
        return 'high'

if __name__ == '__main__':
    print(NumberCategorizer.categorize(5))
    print(NumberCategorizer.categorize(35))
    print(NumberCategorizer.categorize(100))
    print(NumberCategorizer.categorize(0))
    print(NumberCategorizer.categorize(49))
    print(NumberCategorizer.categorize(50))