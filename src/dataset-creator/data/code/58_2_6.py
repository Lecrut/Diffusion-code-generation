from datetime import datetime, timezone
class DateUtils:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        try:
            start_date = datetime.strptime(start_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_str, "%Y-%m-%d")
            start_date_aware = datetime(start_date.year, start_date.month, start_date.day, tzinfo=timezone.utc)
            end_date_aware = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59, tzinfo=timezone.utc)
            delta = end_date_aware - start_date_aware
            return int(delta.days + (delta.seconds // 86400)) if delta.total_seconds() > 0 else 0
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got '{start_str}' or '{end_str}'.") from e
if __name__ == '__main__':
    start_date = "2023-10-05"
    end_date = "2024-01-15"
    days_elapsed = DateUtils.compute_days_elapsed(start_date, end_date)
    print(f"{days_elapsed} days elapsed")