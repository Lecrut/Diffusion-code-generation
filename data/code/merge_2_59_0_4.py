import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-06-17",
        "2025-01-01"
    ]
    for date_str in sample_dates:
        day_number = get_day_of_week(date_str)
        print(f"{date_str} is a {day_number}.")