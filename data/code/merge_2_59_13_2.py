import datetime
def get_weekday(date_str: str) -> int:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.")
if __name__ == '__main__':
    test_dates = ["2023-10-05", "2024-06-17", "2025-01-01"]
    for d in test_dates:
        print(f"{d} -> {get_weekday(d)}")