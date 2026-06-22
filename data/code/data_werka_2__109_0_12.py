import datetime

class MonthCalculator:
    DAYS_IN_WEEK = 7
    MIN_YEAR = 1

    @staticmethod
    def _get_days_in_month(year, month):
        if month == 12:
            next_month = datetime.date(year + 1, 1, 1)
        else:
            next_month = datetime.date(year, month + 1, 1)
        current_month_end = next_month - datetime.timedelta(days=1)
        return current_month_end.day

    @staticmethod
    def calculate_remaining_days(year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if year < MonthCalculator.MIN_YEAR:
            raise ValueError("Year must be positive")
        
        total_days = MonthCalculator._get_days_in_month(year, month)
        
        if day > total_days:
            raise ValueError("Day is out of range for the given month")
        
        current_date = datetime.date(year, month, day)
        month_end_date = datetime.date(year, month, total_days)
        
        remaining = (month_end_date - current_date).days + 1
        return remaining

if __name__ == '__main__':
    test_cases = [
        (2023, 2, 15),
        (2024, 2, 29),
        (2023, 12, 31),
        (2023, 1, 1)
    ]
    
    for y, m, d in test_cases:
        result = MonthCalculator.calculate_remaining_days(y, m, d)
        print(result)