from datetime import date, timedelta

class DateRangeChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(dt: date) -> bool:
        return dt.weekday() in DateRangeChecker.WEEKEND_DAYS

    @classmethod
    def is_weekend_in_range(cls, start_date: date, end_date: date) -> bool:
        current_date = start_date
        while current_date <= end_date:
            if cls.is_weekend(current_date):
                return True
            current_date += timedelta(days=1)
        return False
if __name__ == '__main__':
    print(DateRangeChecker.is_weekend_in_range(date(2023, 4, 1), date(2023, 4, 7)))