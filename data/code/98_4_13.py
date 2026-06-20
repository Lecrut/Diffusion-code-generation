class NumberCategorizer:
    def categorize(self, n):
        return 'low' if n < 10 else ('medium' if n < 50 else 'high')

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    print(categorizer.categorize(5))
    print(categorizer.categorize(35))
    print(categorizer.categorize(100))