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
                if start_dt.tzinfo != end_dt.tzinfo:
                    from datetime import timedelta
                    def normalize_to_utc(dt):
                        return dt.astimezone(timezone.utc)
                    start_dt = normalize_to_utc(start_dt)
                    end_dt = normalize_to_utc(end_dt)
            delta = end_dt - start_dt
            return delta.days
        except ValueError as e:
            raise ValueError(f"Invalid date format provided. Expected YYYY-MM-DD or ISO 8601 with timezone.") from e
if __name__ == '__main__':
    test_cases = [
        ("2023-01-01", "2023-01-05"),
        ("2023-06-15 10:00:00+00:00", "2023-07-14 10:00:00+00:00"),
        ("2023-09-10T08:30:00Z", "2023-09-15T08:30:00Z"),
    ]
    for start_str, end_str in test_cases:
        days = DateUtility.compute_days_elapsed(start_str, end_str)
        print(f"Start: {start_str}, End: {end_str} -> Days elapsed: {days}")