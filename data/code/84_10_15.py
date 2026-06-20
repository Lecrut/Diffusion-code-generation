class DateCalculator:

    def __init__(self):
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def get_day_of_year(self, year, month, day):
        if not 1 <= month <= 12 or not 1 <= day <= self.month_days[month - 1]:
            raise ValueError('Invalid date')
        if month > 2 and self.is_leap_year(year):
            return sum(self.month_days[:month]) + day + 1
        else:
            return sum(self.month_days[:month]) + day
if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_year(2023, 10, 27))