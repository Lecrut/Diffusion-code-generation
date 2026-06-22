import calendar
import datetime

DAY_INDEX_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_day_of_week(year: int, month: int, day: int) -> str:
    date_obj = datetime.date(year, month, day)
    weekday_index = date_obj.weekday()
    return DAY_INDEX_MAP[weekday_index]

if __name__ == '__main__':
    result = get_day_of_week(2025, 3, 15)
    print(result)