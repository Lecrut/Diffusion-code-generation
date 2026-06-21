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

        return f"Number: {number}, Category: {category}, Parity: {parity}"

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    
    sample_numbers = [-5, 0, 3, 12, 27]
    for number in sample_numbers:
        result = categorizer.categorize(number)
        print(result)