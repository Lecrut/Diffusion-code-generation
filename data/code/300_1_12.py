import calendar

class MonthDays:

    def __init__(self, year: int):
        self.year = year
        if not isinstance(self.year, int) or self.year < 1:
            raise ValueError('Year must be a positive integer')

    def days_in_month(self, month: int) -> int:
        if month < 1 or month > 12:
            raise ValueError('Month must be between 1 and 12')
        return calendar.monthrange(self.year, month)[1]
if __name__ == '__main__':
    year = 2023
    month_days = MonthDays(year)
    print(month_days.days_in_month(1))
    print(month_days.days_in_month(2))
    print(month_days.days_in_month(12))