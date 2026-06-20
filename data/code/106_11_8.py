class YearDifferenceCalculator:
    @staticmethod
    def parse_date(date_str):
        return int(date_str.split('-')[0])

    @staticmethod
    def calculate_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '1998-12-25'
    try:
        y1 = YearDifferenceCalculator.parse_date(date1)
        y2 = YearDifferenceCalculator.parse_date(date2)
        difference = YearDifferenceCalculator.calculate_difference(y1, y2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter date strings in 'YYYY-MM-DD' format.")