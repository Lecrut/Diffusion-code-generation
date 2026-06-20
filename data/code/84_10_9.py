class DateCalculator:

    def get_day_of_year(self, year, month, day):
        if not self.is_valid_date(year, month, day):
            raise ValueError('Invalid date')
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year(year):
            days_in_month[1] = 29
        day_of_year = sum(days_in_month[:month - 1]) + day
        return day_of_year

    def is_valid_date(self, year, month, day):
        if not 1 <= month <= 12 or not 1 <= day <= 31:
            return False
        if month == 2 and day > 29:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        return True

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_year(2023, 10, 27))
    print(calculator.get_day_of_year(2020, 10, 27))
    print(calculator.get_day_of_year(2021, 10, 27))