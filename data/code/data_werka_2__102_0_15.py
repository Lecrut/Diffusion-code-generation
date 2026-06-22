import datetime

def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    year_str, month_str, day_str = parts
    if len(year_str) != 4 or len(month_str) != 2 or len(day_str) != 2:
        raise ValueError("Invalid date format")
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        raise ValueError("Invalid date format")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date format")
    weekday_index = date_obj.weekday()
    is_weekday_flag = weekday_index < 5
    return is_weekday_flag

if __name__ == '__main__':
    test_dates = ["2024-01-15", "2024-01-20", "2024-02-30", "2024-13-01", "2024-01-1"]
    for current_date in test_dates:
        try:
            result = is_weekday(current_date)
            print(f"{current_date}: {result}")
        except ValueError as e:
            print(f"{current_date}: Error - {e}")