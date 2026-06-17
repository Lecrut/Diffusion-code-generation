from datetime import datetime, timezone
class DateUtility:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        def parse_date(date_str: str) -> datetime:
            try:
                return datetime.fromisoformat(date_str).astimezone(timezone.utc)
            except ValueError:
                try:
                    dt = datetime.strptime(date_str, "%Y-%m-%d")
                    return dt.replace(tzinfo=timezone.utc)                                
                except ValueError:
                    raise ValueError(f"Invalid date string format: {date_str}")
        start_dt = parse_date(start_str)
        end_dt = parse_date(end_str)
        delta = end_dt - start_dt
        return delta.days
if __name__ == '__main__':
    sample_start = "2023-10-05"
    sample_end = "2024-01-15T18:30+00:00"
    days = DateUtility.compute_days_elapsed(sample_start, sample_end)
    print(days)