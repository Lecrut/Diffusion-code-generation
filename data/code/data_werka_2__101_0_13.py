import datetime
import calendar

def get_day_of_week(date_str):
    try:
        parts = date_str.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        date_obj = datetime.date(year, month, day)
        return calendar.day_name[date_obj.weekday()]
    except (ValueError, IndexError):
        raise ValueError("Date string must be in YYYY-MM-DD format.")

if __name__ == '__main__':
    target = "2023-10-05"
    print(get_day_of_week(target))