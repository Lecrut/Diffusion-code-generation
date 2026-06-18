from datetime import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.weekday()
    except ValueError as e:
        raise ValueError(f"Invalid date format '{date_string}'. Expected 'YYYY-MM-DD'.") from e
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-06-15",
        "2025-12-31"
    ]
    for date_str in sample_dates:
        try:
            day_index = get_day_of_week(date_str)
            days_map = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"{date_str} is a {days_map[day_index]}")
        except ValueError as ve:
            print(ve)