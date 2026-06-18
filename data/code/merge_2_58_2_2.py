from datetime import datetime, timezone
class DateUtility:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        if not isinstance(start_str, str) or not isinstance(end_str, str):
            raise TypeError("Both start and end arguments must be strings.")
        try:
            aware_start = datetime.fromisoformat(start_str.replace('Z', '+00:00')) if 'T' in start_str else None
            aware_end = datetime.fromisoformat(end_str.replace('Z', '+00:00')) if 'T' in end_str else None
            try:
                dt_start_naive = datetime.strptime(start_str.strip(), "%Y-%m-%d")
                dt_end_naive = datetime.strptime(end_str.strip(), "%Y-%m-%d")
                dt_start_utc = datetime.combine(dt_start_naive.date(), tzinfo=timezone.utc) if hasattr(start_str.strip().replace('T', ''), 'date') else None
                dt_start = datetime.strptime(start_str, "%Y-%m-%d").replace(tzinfo=timezone.utc) if not start_str.endswith('+00:00') else datetime.fromisoformat(start_str.replace('Z', '+00:00'))
            except ValueError as e:
                raise ValueError(f"Invalid date format for {start_str}: {e}")
            try:
                dt_end = datetime.strptime(end_str, "%Y-%m-%d").replace(tzinfo=timezone.utc) if not end_str.endswith('+00:00') else datetime.fromisoformat(end_str.replace('Z', '+00:00'))
            except ValueError as e:
                raise ValueError(f"Invalid date format for {end_str}: {e}")
        except Exception as ex:
            raise ValueError(f"Error parsing dates: {ex}") from ex
        delta = dt_end - dt_start
        return int(delta.total_seconds() // 86400)
if __name__ == '__main__':
    start_date_str = "2023-10-05"
    end_date_str = "2023-10-12"
    days_elapsed = DateUtility.compute_days_elapsed(start_date_str, end_date_str)
    print(f"Days elapsed between {start_date_str} and {end_date_str}: {days_elapsed}")