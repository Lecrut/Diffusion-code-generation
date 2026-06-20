class DateCalculator:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 29 if self.is_leap_year(year) else 28

    def calculate_day_of_year(self):
        day_of_year = sum(self.days_in_month(m, 2023) for m in range(1, self.month)) + self.day
        return day_of_year

if __name__ == '__main__':
    date_calculator = DateCalculator(4, 15)
    print(date_calculator.calculate_day_of_year())