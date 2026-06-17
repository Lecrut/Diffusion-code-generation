from datetime import datetime, timezone
class DateUtility:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        try:
            start_dt = datetime.fromisoformat(start_str)
            end_dt = datetime.fromisoformat(end_str)
            if start_dt.tzinfo is None and end_dt.tzinfo is not None:
                start_dt = start_dt.replace(tzinfo=timezone.utc)
            elif start_dt.tzinfo is not None and end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
            else:
                if start_dt.tzinfo != timezone.utc:
                    start_dt = start_dt.astimezone(timezone.utc)
                if end_dt.tzinfo != timezone.utc:
                    end_dt = end_dt.astimezone(timezone.utc)
            delta = end_dt - start_dt
            return delta.days
        except ValueError as e:
            raise ValueError(f"Invalid date format provided. Expected YYYY-MM-DD or ISO 8601 with optional timezone.") from e
if __name__ == '__main__':
    test_cases = [
        ("2023-01-01", "2023-01-05"),
        ("2023-06-15T10:00:00", "2023-07-15T10:00:00+05:00"),                                     
        ("2024-02-29", "2024-03-01"),                  
    ]
    for start_date, end_date in test_cases:
        days = DateUtility.compute_days_elapsed(start_date, end_date)
        print(f"Days between {start_date} and {end_date}: {days}")