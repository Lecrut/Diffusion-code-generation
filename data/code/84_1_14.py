class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif self.is_leap_year():
            return 29
        else:
            return 28

    def day_of_year(self):
        days = sum(self.days_in_month(m) for m in range(1, self.month))
        return days + self.day

if __name__ == '__main__':
    calculator = DateCalculator(2023, 4, 15)
    print(calculator.day_of_year())