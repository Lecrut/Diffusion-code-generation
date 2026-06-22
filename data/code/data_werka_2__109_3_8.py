import calendar
from datetime import datetime, date

class MonthCalendarAnalyzer:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        _, self.days_in_month = calendar.monthrange(self.year, self.month)

    def days_left_in_month(self, current_day: int) -> int:
        return self.days_in_month - current_day

def calculate_remaining_days(year: int, month: int, day: int) -> int:
    analyzer = MonthCalendarAnalyzer(year, month)
    return analyzer.days_left_in_month(day)

if __name__ == '__main__':
    year_val = 2023
    month_val = 10
    day_val = 15
    remaining = calculate_remaining_days(year_val, month_val, day_val)
    print(remaining)
    analyzer = MonthCalendarAnalyzer(2023, 10)
    print(analyzer.days_in_month)
    print(analyzer.days_left_in_month(15))