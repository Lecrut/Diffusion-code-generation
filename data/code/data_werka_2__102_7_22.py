import calendar
from datetime import date

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def is_weekday(d):
    try:
        day_index = calendar.weekday(d.year, d.month, d.day)
        return day_index < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    sample_date = date(2024, 5, 15)
    result = is_weekday(sample_date)
    print(result)