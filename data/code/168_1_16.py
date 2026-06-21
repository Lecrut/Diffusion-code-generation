class NumberCategorizer:
    EVEN = 'Even'
    ODD = 'Odd'

    @staticmethod
    def categorize_numbers(numbers):
        categorized = {NumberCategorizer.EVEN: [], NumberCategorizer.ODD: []}
        for number in numbers:
            if int(number) % 2 == 0:
                categorized[NumberCategorizer.EVEN].append(int(number))
            else:
                categorized[NumberCategorizer.ODD].append(int(number))
        return categorized

if __name__ == '__main__':
    sample_numbers = ['1', '2', '3', '4', '5', '6']
    result = NumberCategorizer.categorize_numbers(sample_numbers)
    print(result)