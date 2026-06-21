import datetime
import calendar

DAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def get_day_of_week(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    weekday_index = date_obj.weekday()
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)