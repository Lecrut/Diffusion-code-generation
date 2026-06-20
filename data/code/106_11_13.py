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
    sample_date1 = "2023-04-15"
    sample_date2 = "1998-12-25"
    
    year1 = calculator.parse_date(sample_date1)
    year2 = calculator.parse_date(sample_date2)
    
    difference = calculator.calculate_difference(year1, year2)
    print(difference)