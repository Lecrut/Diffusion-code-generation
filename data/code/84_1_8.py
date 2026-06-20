class DateCalculator:

    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day

    def is_leap_year(self, year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_in_month(self, year: int, month: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        else:
            raise ValueError('Invalid month')

    def day_of_year(self, year: int) -> int:
        total_days = sum((self.days_in_month(year, m) for m in range(1, self.month)))
        return total_days + self.day
if __name__ == '__main__':
    calculator = DateCalculator(month=2, day=29)
    print(calculator.day_of_year(year=2024))