class DateDifferenceCalculator:
    def calculate_year_difference(self, date1, date2):
        year1 = int(date1.split('-')[0])
        year2 = int(date2.split('-')[0])
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_year_difference('2023-04-30', '1990-05-01'))
    print(calculator.calculate_year_difference('2000-12-25', '2024-01-01'))
    print(calculator.calculate_year_difference('1850-07-04', '1900-01-01'))