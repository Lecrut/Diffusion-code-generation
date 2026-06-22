import datetime

class MonthCalculator:
    DAYS_IN_WEEK = 7
    MIN_YEAR = 1
    MAX_YEAR = 9999

    @staticmethod
    def _get_last_day_of_month(year, month):
        if month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, month + 1, 1)
        return next_month_start - datetime.timedelta(days=1)

    @staticmethod
    def calculate_days_remaining(year, month):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if year < MonthCalculator.MIN_YEAR or year > MonthCalculator.MAX_YEAR:
            raise ValueError("Year out of range")
        
        last_day = MonthCalculator._get_last_day_of_month(year, month)
        today = datetime.date.today()
        
        if today > last_day:
            return 0
        
        return (last_day - today).days

if __name__ == '__main__':
    sample_dates = [
        (2023, 10),
        (2024, 2),
        (2024, 12),
        (2025, 1)
    ]
    
    for y, m in sample_dates:
        result = MonthCalculator.calculate_days_remaining(y, m)
        print(result)