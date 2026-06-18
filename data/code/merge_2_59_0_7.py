from datetime import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-06-18",
        "2025-12-31"
    ]
    for date_str in sample_dates:
        day_num = get_day_of_week(date_str)
        days_map = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"{date_str} is a {days_map[day_num]}")