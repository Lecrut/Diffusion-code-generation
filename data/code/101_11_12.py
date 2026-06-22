import datetime

WEEKDAY_NAMES = {
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
    return WEEKDAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)