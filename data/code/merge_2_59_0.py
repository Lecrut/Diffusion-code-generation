from datetime import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-15", "2025-12-31"]
    for date_str in sample_dates:
        day_number = get_day_of_week(date_str)
        days_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        print(f"Date: {date_str} -> Day Number: {day_number}, Full Name: {days_map[day_number]}")