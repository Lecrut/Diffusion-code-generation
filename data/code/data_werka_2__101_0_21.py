import datetime
import calendar

def get_weekday(date_str):
    try:
        parts = date_str.split("-")
        if len(parts) != 3:
            raise ValueError("Incorrect date format")
        year, month, day = (int(p) for p in parts)
        date_obj = datetime.date(year, month, day)
        return calendar.day_name[date_obj.weekday()]
    except ValueError as e:
        raise ValueError(f"Invalid date: {date_str}") from e

if __name__ == '__main__':
    date_str = "2023-10-05"
    weekday_name = get_weekday(date_str)
    print(weekday_name)