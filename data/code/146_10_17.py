class NumberCategorizer:
    def categorize(self, number):
        if number < 0:
            category = 'negative'
        elif number == 0:
            category = 'zero'
        else:
            category = 'positive'

        if number % 2 == 0:
            parity = 'even'
        else:
            parity = 'odd'

        return f"{category}, {parity}"

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    numbers = [-5, 0, 3, 10]
    for number in numbers:
        result = categorizer.categorize(number)
        print(f"Number: {number}, Category: {result}")