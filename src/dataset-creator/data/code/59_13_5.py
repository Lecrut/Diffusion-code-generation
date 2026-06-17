from datetime import date
def get_weekday(date_str: str) -> int:
    try:
        parsed_date = date.fromisoformat(date_str.replace('-', ''))
        return parsed_date.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got {date_str}")
if __name__ == '__main__':
    test_dates = ["2023-10-05", "2024-01-01", "2023-12-25"]
    for d in test_dates:
        print(f"{d} -> {get_weekday(d)}")