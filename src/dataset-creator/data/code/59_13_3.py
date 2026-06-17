import datetime
def get_weekday_from_date(date_str: str) -> int:
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-17", "2025-01-01"]
    for d in sample_dates:
        print(f"{d}: {get_weekday_from_date(d)}")