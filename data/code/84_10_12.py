class DateCalculator:

    def get_day_of_year(self, year, month, day):
        if month < 1 or month > 12 or day < 1:
            return 'Invalid date'
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            month_days[2] = 29
        day_of_year = sum(month_days[:month]) + day
        return day_of_year
if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_year(2023, 10, 27))