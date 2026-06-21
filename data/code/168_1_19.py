class NumberCategorizer:
    def __init__(self):
        self.even_numbers = []
        self.odd_numbers = []

    def categorize(self, numbers):
        for number in numbers:
            if number % 2 == 0:
                self.even_numbers.append(number)
            else:
                self.odd_numbers.append(number)

    def get_results(self):
        return {'even': self.even_numbers, 'odd': self.odd_numbers}

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    sample_numbers = [10, 23, 45, 68, 90, 17]
    categorizer.categorize(sample_numbers)
    print(categorizer.get_results())