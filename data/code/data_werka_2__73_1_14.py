from datetime import datetime, timedelta

class DateDiffCalculator:
    _FORMAT_PATTERN = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def _parse_iso(date_string: str) -> datetime:
        if 'T' not in date_string:
            raise ValueError("Invalid ISO 8601 format: missing 'T' separator")
        return datetime.fromisoformat(date_string)

    @staticmethod
    def calculate_time_diff(date_string1: str, date_string2: str) -> timedelta:
        dt1 = DateDiffCalculator._parse_iso(date_string1)
        dt2 = DateDiffCalculator._parse_iso(date_string2)
        return dt2 - dt1

if __name__ == '__main__':
    start_date = "2023-06-15T08:00:00"
    end_date = "2023-06-20T17:30:00"
    result = DateDiffCalculator.calculate_time_diff(start_date, end_date)
    print(result)