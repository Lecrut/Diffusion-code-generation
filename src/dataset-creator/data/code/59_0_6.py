import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.weekday()
    except ValueError:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'")
if __name__ == '__main__':
    sample_dates = ['2023-10-05', '2024-07-20', '1999-12-31']
    for date_str in sample_dates:
        try:
            day_num = get_day_of_week(date_str)
            days_map = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            print(f"{date_str} -> {days_map[day_num]}")
        except ValueError as e:
            print(e)