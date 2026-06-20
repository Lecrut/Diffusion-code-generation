class DateCalculator:

    def __init__(self):
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def set_days_in_month_for_year(self, year):
        if self.is_leap_year(year):
            self.days_in_month[2] = 29
        else:
            self.days_in_month[2] = 28

    def calculate_day_of_year(self, month, day):
        if not 1 <= month <= 12:
            raise ValueError('Month must be between 1 and 12.')
        if not 1 <= day <= self.days_in_month[month]:
            raise ValueError(f'Day must be between 1 and {self.days_in_month[month]} for the given month.')
        day_of_year = sum(self.days_in_month[:month]) + day
        return day_of_year
if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_day_of_year(1, 1))
    print(calculator.calculate_day_of_year(2, 29))
    print(calculator.calculate_day_of_year(3, 15))
    print(calculator.calculate_day_of_year(12, 31))