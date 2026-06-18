from datetime import date, datetime
def calculate_days_delta(start: str | datetime | None = None, end: str | datetime | None = None) -> int:
    def parse_date(d):
        if isinstance(d, (datetime, date)):
            return d
        elif isinstance(d, str):
            try:
                return datetime.fromisoformat(d).date()
            except ValueError:
                raise TypeError(f"Invalid date string format. Expected ISO 8601.") from None
        else:
            raise TypeError("Input must be a datetime object or an ISO formatted string.")
    start_date = parse_date(start) if start is not None else datetime.now().date()
    end_date = parse_date(end) if end is not None else (datetime.now().date())
    delta_days = int((end_date - start_date).days)
    return abs(delta_days)
if __name__ == '__main__':
    result_str = calculate_days_delta("2023-01-01", "2024-06-01")
    from datetime import date as dt_date
    start_dt = dt_date(2023, 5, 15)
    end_dt = dt_date(2023, 8, 15)
    result_obj = calculate_days_delta(start_dt, end_dt)
    print(f"Days between '2023-01-01' and '2024-06-01': {result_str}")
    print(f"Days between 2023-05-15 and 2023-08-15: {result_obj}")