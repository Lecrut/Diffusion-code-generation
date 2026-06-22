import datetime
import calendar

def get_day_of_week(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Invalid date format")
    try:
        y = int(year)
        m = int(month)
        d = int(day)
    except ValueError:
        raise ValueError("Invalid date format")
    if m < 1 or m > 12 or d < 1 or d > 31:
        raise ValueError("Invalid date format")
    try:
        date_obj = datetime.date(y, m, d)
    except ValueError:
        raise ValueError("Invalid date format")
    day_index = date_obj.weekday()
    return calendar.day_name[day_index]

if __name__ == '__main__':
    target_date = "2023-10-05"
    day_name = get_day_of_week(target_date)
    print(day_name)