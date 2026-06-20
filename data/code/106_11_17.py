class DateDifferenceCalculator:
    @staticmethod
    def parse_date(date_str):
        year, month, day = map(int, date_str.split('-'))
        return year

    @staticmethod
    def calculate_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date1 = "2023-04-01"
    date2 = "1998-05-15"
    try:
        y1 = calculator.parse_date(date1)
        y2 = calculator.parse_date(date2)
        difference = calculator.calculate_difference(y1, y2)
        print(difference)
    except ValueError:
        print("Invalid input: Please enter valid date strings.")