from datetime import date, timezone, timedelta
class DateUtility:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        if not isinstance(start_str, str) or not isinstance(end_str, str):
            raise TypeError("Both start and end arguments must be strings.")
        try:
            from dateutil import parser
            start_dt = parser.parse(start_str).replace(tzinfo=timezone.utc) if hasattr(parser.parse(start_str), 'tzinfo') else None
            end_dt = parser.parse(end_str).replace(tzinfo=timezone.utc) if hasattr(parser.parse(end_str), 'tzinfo') else None
        except Exception:
            from datetime import datetime
            start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
            return (end_date - start_date).days
if __name__ == '__main__':
    sample_start = "2023-10-05"
    sample_end = "2024-01-15"
    days_diff = DateUtility.compute_days_elapsed(sample_start, sample_end)
    print(f"Days elapsed between {sample_start} and {sample_end}: {days_diff}")