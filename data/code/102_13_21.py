from datetime import date
from datetime import datetime

class WeekdayChecker:
    BUSINESS_START = 0
    BUSINESS_END = 4

    @staticmethod
    def is_monday_to_friday(d: date) -> bool:
        if isinstance(d, datetime):
            d = d.date()
        if not isinstance(d, date):
            raise TypeError("Expected a date or datetime instance")
        day_index = d.weekday()
        return WeekdayChecker.BUSINESS_START <= day_index <= WeekdayChecker.BUSINESS_END

if __name__ == '__main__':
    checker = WeekdayChecker()
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        date(2023, 10, 29),
        datetime(2023, 10, 23, 12, 0),
    ]
    for dt in test_cases:
        result = WeekdayChecker.is_monday_to_friday(dt)
        print(result)