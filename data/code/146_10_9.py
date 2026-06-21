class NumberCategorizer:
    NEGATIVE = "negative"
    ZERO = "zero"
    POSITIVE = "positive"
    EVEN = "even"
    ODD = "odd"

    @staticmethod
    def categorize(number):
        if number < 0:
            return NumberCategorizer.NEGATIVE
        elif number == 0:
            return NumberCategorizer.ZERO
        else:
            category = NumberCategorizer.POSITIVE
            if number % 2 == 0:
                category += ", " + NumberCategorizer.EVEN
            else:
                category += ", " + NumberCategorizer.ODD
            return category

if __name__ == '__main__':
    categorizer = NumberCategorizer()
    numbers = [-10, 0, 5, 27]
    for number in numbers:
        result = categorizer.categorize(number)
        print(f"Number: {number}, Category: {result}")