import calendar
from datetime import date

DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def find_day_name(year, month, day):
    target_date = date(year, month, day)
    weekday_index = target_date.weekday()
    return DAYS_OF_WEEK[weekday_index]

if __name__ == '__main__':
    YEAR = 2023
    MONTH = 12
    DAY = 25
    computed_day = find_day_name(YEAR, MONTH, DAY)
    print(computed_day)