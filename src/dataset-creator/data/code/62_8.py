import datetime
def add_months_to_date(current_year: int = None, current_month: int = None, days_offset: int = 0) -> tuple:
    if not (1 <= current_month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    try:
        base_datetime = datetime.datetime(current_year, current_month, 15).replace(hour=14, minute=30)
        target_date = base_datetime + datetime.timedelta(days=days_offset)
        return {
            "datetime": str(target_date),
            "timestamp": int(target_date.timestamp())
        }
    except ValueError as e:
        raise RuntimeError("Invalid input provided.") from e
if __name__ == '__main__':
    result = add_months_to_date(2023, 6)
    print(result["datetime"])
    print(result["timestamp"])