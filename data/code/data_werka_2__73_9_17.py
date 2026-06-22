from datetime import datetime, timedelta
import calendar

class DateIntervalCalculator:
    DATE_FORMAT = '%Y-%m-%d'
    SECONDS_IN_DAY = 86400

    @staticmethod
    def _parse_date(date_string: str) -> datetime:
        try:
            return datetime.strptime(date_string, DateIntervalCalculator.DATE_FORMAT)
        except ValueError as e:
            raise ValueError(f"Invalid date string: {date_string}") from e

    @classmethod
    def calculate_days(cls, start_date_str: str, end_date_str: str) -> int:
        start_dt = cls._parse_date(start_date_str)
        end_dt = cls._parse_date(end_date_str)
        delta = end_dt - start_dt
        return delta.days

if __name__ == '__main__':
    start = '2023-01-01'
    end = '2023-12-31'
    days = DateIntervalCalculator.calculate_days(start, end)
    print(days)