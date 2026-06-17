from datetime import datetime, timezone
import re
class DateUtility:
    @staticmethod
    def parse_date(date_string: str) -> datetime:
        pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
        match = re.match(pattern, date_string.strip())
        if not match:
            raise ValueError(f"Invalid date format '{date_string}'. Expected YYYY-MM-DD.")
        year, month, day = map(int, match.groups())
        return datetime(year, month, day)
    @staticmethod
    def compute_days_elapsed(start_date_str: str, end_date_str: str) -> int:
        start_dt = DateUtility.parse_date(start_date_str)
        end_dt = DateUtility.parse_date(end_date_str)
        delta = end_dt - start_dt
        return delta.days
if __name__ == '__main__':
    sample_start = "2023-10-05"
    sample_end = "2023-10-12"
    days_diff = DateUtility.compute_days_elapsed(sample_start, sample_end)
    print(f"Days elapsed between {sample_start} and {sample_end}: {days_diff}")