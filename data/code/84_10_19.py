class DateCalculator:
    def get_day_of_year(self, year, month, day):
        if not self.is_valid_date(year, month, day):
            return "Invalid date"
        
        days_in_month = [31, 28 + self.is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_of_year = sum(days_in_month[:month - 1]) + day
        return day_of_year

    def is_valid_date(self, year, month, day):
        if month < 1 or month > 12:
            return False
        if day < 1 or day > self.days_in_month(year, month):
            return False
        return True

    def days_in_month(self, year, month):
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    calculator = DateCalculator()
    day_number = calculator.get_day_of_year(2023, 10, 27)
    print(day_number)