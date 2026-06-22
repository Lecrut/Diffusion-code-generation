from datetime import datetime
from dateutil.relativedelta import relativedelta

class DateComparator:
    WEEK_THRESHOLD = 7

    @staticmethod
    def is_within_one_week(date1: datetime, date2: datetime) -> bool:
        delta = relativedelta(date1, date2)
        total_days = abs(delta.days)
        if delta.months > 0 or delta.years > 0:
            return False
        if total_days >= DateComparator.WEEK_THRESHOLD:
            return False
        if delta.days == -DateComparator.WEEK_THRESHOLD:
            return False
        return True

if __name__ == '__main__':
    date_a = datetime(2023, 10, 1, 12, 0, 0)
    date_b = datetime(2023, 10, 8, 12, 0, 0)
    comparison = DateComparator()
    result = comparison.is_within_one_week(date_a, date_b)
    print(result)