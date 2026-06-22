import calendar
from datetime import datetime, timedelta

class MonthCalculator:
    DAYS_IN_WEEK = 7
    DAYS_IN_MONTH_OFFSET = 1

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return calendar.isleap(year)

    @classmethod
    def calculate_days_left(cls, year: int, month: int, day: int) -> int:
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        
        total_days = cls.get_days_in_month(year, month)
        
        if day > total_days:
            raise ValueError("Day out of range for month")
            
        current_date = datetime(year, month, day)
        next_month_start = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
        
        delta = next_month_start - current_date
        return delta.days

if __name__ == '__main__':
    calc = MonthCalculator()
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    days_remaining = calc.calculate_days_left(sample_year, sample_month, sample_day)
    print(days_remaining)