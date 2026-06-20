class NumberCategorizer:
    LOW_THRESHOLD = 10
    MEDIUM_THRESHOLD = 50

    @staticmethod
    def categorize_number(n):
        if n < NumberCategorizer.LOW_THRESHOLD:
            return 'low'
        elif n < NumberCategorizer.MEDIUM_THRESHOLD:
            return 'medium'
        else:
            return 'high'

if __name__ == '__main__':
    print(NumberCategorizer.categorize_number(5))
    print(NumberCategorizer.categorize_number(35))
    print(NumberCategorizer.categorize_number(100))
    print(NumberCategorizer.categorize_number(9))
    print(NumberCategorizer.categorize_number(50))
    print(NumberCategorizer.categorize_number(51))